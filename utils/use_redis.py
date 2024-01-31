# @Project : token
# @Time : 2022/12/23 11:05
# @Author : Alan
# @File : redis.py

import time
import redis
from utils.logger import logger


class RedisError(Exception):
    pass


class Redis:
    def __init__(self, host, port, db, password=None, decode_responses=True):
        for i in range(3):
            try:
                logger.info(f"连接redis {host} {port} {db}")
                self.__con = redis.StrictRedis(host=host, port=port, password=password, db=db,
                                               decode_responses=decode_responses)
                # pool = redis.ConnectionPool(host=host, port=port, password=password, db=db,
                #                                decode_responses=decode_responses)
                # self.__con = redis.Redis(connection_pool=pool)
            except Exception as e:
                logger.info("redis连接失败,错误信息为%s" % e)
            else:
                break
            time.sleep(1)
        else:
            raise RedisError("redis连接失败")

    def coon(self):
        return self.__con

    def set_value(self, key, value, ex=None):
        """
        设置key的值
        :param key: 键值
        :param value: value值
        :param ex: 过期时间 （秒）
        :return:
        """
        return self.__con.set(name=key, value=value, ex=ex)

    def get_value(self, key):
        """
        获取 key 的值，如果key不存在则返回None
        :param key: key值
        :return:
        """
        logger.info(f"[redis] 获取值key: {key}")
        return self.__con.get(key)

    def get_keys(self, pattern="*"):
        """
        获取所有key
        :param pattern: 模式
        :return: 返回所有key的列表
        """
        return self.__con.keys(pattern)

    def hset_key(self, name, key, value):
        return self.__con.hset(name=name, key=key, value=value)

    def flush_all(self):
        self.__con.flushall()


class HandleLocalRedis:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, host, port, db, password=None, decode_responses=True):
        for i in range(3):
            try:
                logger.info(f"连接redis {host} {port} {db}")
                self.__con = redis.StrictRedis(host=host, port=port, password=password, db=db,
                                               decode_responses=decode_responses)
                # pool = redis.ConnectionPool(host=host, port=port, password=password, db=db,
                #                                decode_responses=decode_responses)
                # self.__con = redis.Redis(connection_pool=pool)
            except Exception as e:
                logger.info("redis连接失败,错误信息为%s" % e)
            else:
                break
            time.sleep(1)
        else:
            raise RedisError("redis连接失败")

    def coon(self):
        return self.__con

    def set_value(self, key, value, ex=None):
        """
        设置key的值
        :param key: 键值
        :param value: value值
        :param ex: 过期时间 （秒）
        :return:
        """
        return self.__con.set(name=key, value=value, ex=ex)

    def get_value(self, key):
        """
        获取 key 的值，如果key不存在则返回None
        :param key: key值
        :return:
        """
        logger.info(f"[redis] 获取值key: {key}")
        return self.__con.get(key)
