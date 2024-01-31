# @Project : token
# @Time : 2022/12/23 10:39
# @Author : Alan
# @File : oauth.py

import requests
from setting import OAUTH_COUNT, REDIS_CONF
from utils.logger import logger
from utils.use_redis import Redis, HandleLocalRedis


class LoginOauth:
    def __init__(self, project, env, username, password, is_cache=True):
        self.project = project
        self.env = env
        self.username = username
        self.password = password
        self.local_redis = HandleLocalRedis(**REDIS_CONF)
        self.is_cache = is_cache
        self.session = requests.session()

    @property
    def _config(self):
        config = OAUTH_COUNT
        return config[self.project][self.env]

    @property
    def _cache_key(self):
        return self.project + ":" + self.env + ":" + self.username

    def get_image_captcha_code(self, key):
        """获取图片验证码"""
        logger.info("从redis获取图片验证码")
        redis_conf = self._config['redis']
        redis = Redis(**redis_conf)
        key = 'captcha_codes:' + key
        code = redis.get_value(key)
        logger.info(f"图片验证码: {code}")
        return code

    def _redirects(self, location):
        """获取重定向location中的code"""
        logger.info(f"请求重定向地址，获取最终的code {location}")
        if "?code" in location:
            logger.info(f"location code {location}")
            code = location.split('=')[-1]
            return code
        res = self.session.get(url=location, allow_redirects=False)
        print("url---------------", location)
        location = res.headers.get('location')
        return self._redirects(location)

    def cache_token(self, token):
        key = self._cache_key
        logger.info(f"将token缓存到redis kye: {key}, value: {token}")
        self.local_redis.set_value(key, token, ex=1000)

    def get_cache_token(self):
        key = self._cache_key
        logger.info(f"获取缓存token key: {key}")
        token = self.local_redis.get_value(key)
        logger.info(f"获取结果: {token}")
        return token

    def request_token(self):
        """请求oauth获取token"""
        logger.info("------------ 向oauth请求token -------------")
        oauth_conf = self._config
        token = None
        try:
            # 调用authorize_url请求，获取cookie
            self.session.get(oauth_conf['authorize_url'])
            # 获取图片验证码和uuid
            logger.info(f"获取图片验证码和uuid {oauth_conf['image_url']}")
            headers = {"Accept-Language": "zh-CN,zh;q=0.9"}
            res = self.session.get(url=oauth_conf['image_url'], headers=headers).json()
            logger.info(f"返回结果: {res['data']['uuid']}")
            uuid = res['data']['uuid']
            vcode = self.get_image_captcha_code(uuid)

            login_data = {
                "username": self.username,
                "password": self.password,
                "vcode": eval(vcode),
                "uuid": uuid,
                "user_type": "wdp",
                "autologin": 0
            }
            # 调用登录接口，返回重定向地址
            logger.info(f"调用登录接口，返回重定向地址 {oauth_conf['login_url']}")
            res = self.session.post(url=oauth_conf['login_url'], data=login_data, allow_redirects=False)
            oauth_url = res.headers.get('location')
            # 请求重定向的地址, 获取最终的code

            code = self._redirects(oauth_url)
            logger.info(f"code {code}")

            #先进行get请求code值，获取response中的Etag这个值
            # logger.info(f"111111111111 {oauth_conf['get_login']}")
            url = oauth_conf['get_login'] + "?code=" + code
            res = self.session.get(url=url)
            Etag = res.headers.get('Etag')
            # logger.info(f"获取 Etag 的值: {Etag}")
            # if Etag is None:
            #     Etag = 'W/"25fa-18c84ef2ba0"'

            # 通过code获取token
            logger.info(f"获取{self.project}的token: {oauth_conf['login_oauth_url']}")
            project_token = ProjectToken(self.session, oauth_conf['login_oauth_url'], code, Etag)
            token = getattr(project_token, self.project.lower())()
            logger.info(f"token: {token}")
        except Exception as e:
            logger.error(f'获取token异常: {e}')
        finally:
            self.session.close()
            return token

    def get_token(self, num=3):
        """
        获取token
        :param num: 为了防止因为网络抖动导致获取token失败，这里加了重试；默认重试三次
        :return: token
        """
        # 获取缓存中的token
        if self.is_cache:
            _cache_token = self.get_cache_token()
            if _cache_token:
                return _cache_token
        # 缓存中不存在，请求新的token
        for i in range(num):
            token = self.request_token()
            if token:
                self.cache_token(token)
                return token

        return None

    def oauth_token(self, code):
        params = {
            'grant_type': 'authorization_code',
            'client_id': 'pass_cloud',
            'client_secret': 'XeohHBZxay',
            'code': code,
            'user_type': 'wdp'
        }
        res = self.session.post('http://10.100.10.174:30102/oauth/token', params=params).json()
        print(res)
        return res['data']['token']


class ProjectToken:
    def __init__(self, session, url, code, Etag):
        self.session = session
        self.url = url
        self.code = code
        self.Etag = Etag

    def _token(self, result):
        try:
            if 'token' in result:
                token = result['token']
            elif 'tokens' in result:
                token = result['tokens'][0]
            return token
        except:
            return None

    def paas(self):
        headers = {"If-None-Match": self.Etag}
        response = self.session.post(url=self.url, headers=headers, json={"code": self.code})
        # res = self.session.post(url=self.url, json={"code": self.code})
        print("请求头------：", response.request.headers)
        print("响应头-----------：", response.headers)
        logger.info(f'响应码: {response}')
        logger.info(f'响应结果: {response.text}')
        return self._token(response.json().get('result'))

    def gui(self):
        url = self.url + '&code=' + self.code
        res = self.session.post(url=url)
        logger.info(f'响应结果: {res.text}')
        return self._token(res.json().get('data'))

    def meet(self):
        url = self.url + self.code
        res = self.session.get(url=url)
        logger.info(f'响应结果: {res.text}')
        return self._token(res.json().get('result'))

    def wdp5(self):
        res = self.session.post(url=self.url, json={"code": self.code})
        logger.info(f'响应结果: {res.text}')
        return self._token(res.json().get('results'))

    def daas(self):
        res = self.session.post(url=self.url, json={"code": self.code})
        logger.info(f'响应结果: {res.text}')
        return self._token(res.json().get('result'))
