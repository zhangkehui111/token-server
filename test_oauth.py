# @Project : token
# @Time : 2022/12/23 13:45
# @Author : Alan
# @File : test_oauth.py

import unittest
from parameterized import parameterized
from oauth import LoginOauth

# datas = [
#     ('MEET', 'release', '18256584663', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('MEET', 'stag', '19924539456', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('PAAS', 'release', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('PAAS', 'stag', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('PAAS', 'dev', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('PAAS', 'test', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('PAAS', 'test03', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('PAAS', 'autotest', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'release', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'stag', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'dev', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'test', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'test03', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'pvt_internal', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('GUI', 'autotest', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw=='),
#     ('WDP5', 'release', '15618826227', 'M2im6xRsNasWLqlfoGQC8A=='),
#     ('WDP5', 'test04', '18337111813', '6PgOjBOK97UnvCnd8yfoRQ=='),
#     ('DaaS', 'test04', '18337111813', '6PgOjBOK97UnvCnd8yfoRQ=='),
#     ('DaaS', 'prv', '17777777777', '+/T2OT1qjHjj+Bc+5Idzpw=='),
# ]
#
#
# class TestOauth(unittest.TestCase):
#     @parameterized.expand(datas)
#     def test_get_token(self, project, env, username, password):
#         print(project, env, username, password)
#         res = LoginOauth(project, env, username, password, is_cache=False).get_token()
#         assert res is not None


if __name__ == '__main__':
    # unittest.main()
    res = LoginOauth(project='PAAS', env="release", username='13699038618', password='+/T2OT1qjHjj+Bc+5Idzpw==', is_cache=False).get_token()
    # res = LoginOauth('WDP5', 'release', '15618826227', 'M2im6xRsNasWLqlfoGQC8A==', is_cache=False).get_token()
    # res = LoginOauth('PAAS', 'stag', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw==', is_cache=False).get_token()
    # res = LoginOauth('GUI', 'test03', '13699038618', '+/T2OT1qjHjj+Bc+5Idzpw==', is_cache=False).get_token()
    print(res)