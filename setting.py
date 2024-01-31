# @Project : token
# @Time : 2022/12/23 11:10
# @Author : Alan
# @File : setting.py

from pathlib import Path

# 项目根路径
BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR / 'logs'

OAUTH_COUNT = {
    "MEET": {
        "release": {
            "authorize_url": "https://oauth.51aes.com/oauth/authorize?client_id=meet_client&grant_type=authorization_code&client_secret=YpLiasGP2fo&response_type=code&redirect_uri=https://mspace-ct.51meet.com/",
            "image_url": "https://oauth.51aes.com/captchaImage",
            "login_url": "https://oauth.51aes.com/login",
            "login_oauth_url": "https://mspace.51meet.com/meetapi/api/login/loginByOAuth?code=",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "1",
            }
        },
        "stag": {
            "authorize_url": "https://oauth-staging.51aes.com/oauth/authorize?client_id=meet_client&grant_type=authorization_code&client_secret=YpLiasGP2fo&response_type=code&redirect_uri=https://mspace-staging.51meet.com",
            "image_url": "https://oauth-staging.51aes.com/captchaImage",
            "login_url": "https://oauth-staging.51aes.com/login",
            "login_oauth_url": "https://mspace-staging.51meet.com/meetapi/api/login/loginByOAuth?code=",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "3",
            }
        },
    },
    "PAAS": {
        "release": {
            "authorize_url": "https://oauth.51aes.com/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&client_secret=XeohHBZxay&response_type=code&redirect_uri=https://paas.51aes.com",
            "image_url": "https://oauth.51aes.com/captchaImage?lang=en_US",
            "login_url": "https://oauth.51aes.com/login",
            "get_login": "https://paas.51aes.com/",
            "login_oauth_url": "https://paas.51aes.com/api/login/oauth",
            "redis": {
                "host": "10.22.0.9",
                "password": "EcLiJfJMJDbD00QoPEj4",
                "port": "6379",
                "db": "6",
            }
        },
        "stag": {
            "authorize_url": "https://oauth-staging.51aes.com/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&response_type=code&redirect_uri=https://paas-staging.51aes.com",
            "image_url": "https://oauth-staging.51aes.com/captchaImage",
            "login_url": "https://oauth-staging.51aes.com/login",
            "login_oauth_url": "https://paas-staging.51aes.com/api/login/oauth",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "3",
            }
        },
        "dev": {
            "authorize_url": "http://oauth-dev.51aes.com/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&response_type=code&redirect_uri=http://cloud-paas-dev.51vr.local",
            "image_url": "http://oauth-dev.51aes.com/captchaImage",
            "login_url": "http://oauth-dev.51aes.com/login",
            "login_oauth_url": "http://cloud-paas-dev.51vr.local/api/login/oauth",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "7",
            }
        },
        "test": {
            "authorize_url": "http://oauth-test.51aes.com/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&response_type=code&redirect_uri=http://cloud-paas-test.51vr.local",
            "image_url": "http://oauth-test.51aes.com/captchaImage",
            "login_url": "http://oauth-test.51aes.com/login",
            "login_oauth_url": "http://cloud-paas-test.51vr.local/api/login/oauth",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "5",
            }
        },
        "test03": {
            "authorize_url": "http://oauth-test03.51aes.com/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&response_type=code&redirect_uri=http://cloud-paas-test03.51vr.local",
            "image_url": "http://oauth-test03.51aes.com/captchaImage",
            "login_url": "http://oauth-test03.51aes.com/login",
            "login_oauth_url": "http://cloud-paas-test03.51vr.local/api/login/oauth",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "9",
            }
        },
        "pvt_internal": {
            "authorize_url": "http://10.100.10.152:30601/oauth/authorize?client_id=private_paas_client&grant_type=authorization_code&response_type=code&redirect_uri=http://10.100.10.152:38890",
            "image_url": "http://10.100.10.152:30601/captchaImage?lang=en_US",
            "login_url": "http://10.100.10.152:30601/login",
            "login_oauth_url": "http://10.100.10.152:38890/api/login/oauth",
            "redis": {
                "host": "10.100.10.152",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "31105",
                "db": "4",
            }
        },
        "standalone": {
            "authorize_url": "https://oauth.51aes.com/oauth/authorize?client_id=pass_client&grant_type=authorization_code&response_type=code&redirect_uri=http://10.66.9.143:8890",
            "image_url": "https://oauth.51aes.com/captchaImage?lang=en_US",
            "login_url": "https://oauth.51aes.com/login",
            "login_oauth_url": "http://10.66.9.196:8890/api/login/oauth",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "1",
            }
        },
        "autotest": {
            "authorize_url": "http://10.100.10.174:30102/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&response_type=code&redirect_uri=http://10.100.10.174:32129",
            "image_url": "http://10.100.10.174:30102/captchaImage?lang=en_US",
            "login_url": "http://10.100.10.174:30102/login",
            "login_oauth_url": "http://10.100.10.174:32129/login/oauth",
            "redis": {
                "host": "10.100.10.174",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "31106",
                "db": "7",
            }
        }
    },
    "GUI": {
        "pvt_internal": {
            "authorize_url": "http://10.100.10.152:30601/oauth/authorize?client_id=private_gui_client&grant_type=authorization_code&response_type=code&redirect_uri=http://10.100.10.152:38890",
            "image_url": "http://10.100.10.152:30601/captchaImage?lang=en_US",
            "login_url": "http://10.100.10.152:30601/login",
            "login_oauth_url": "http://10.100.10.152:30601/oauth/token?grant_type=authorization_code&client_id=private_gui_client&client_secret=d41d9743beb24e14b3548471b90825d1",
            "redis": {
                "host": "10.100.10.152",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "31105",
                "db": "4",
            }
        },
        "test": {
            "authorize_url": "http://oauth-test.51aes.com/oauth/authorize?client_id=gui_client&grant_type=authorization_code&response_type=code&redirect_uri=http://wdt-frontend-test.51vr.local",
            "image_url": "http://oauth-test.51aes.com/captchaImage",
            "login_url": "http://oauth-test.51aes.com/login",
            "login_oauth_url": "http://oauth-test.51aes.com/oauth/token?grant_type=authorization_code&client_id=gui_client&client_secret=XswhAJYuK",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "5",
            }
        },
        "dev": {
            "authorize_url": "http://oauth-dev.51aes.com/oauth/authorize?client_id=gui_client&grant_type=authorization_code&response_type=code&redirect_uri=http://wdt-frontend-dev.51vr.local",
            "image_url": "http://oauth-dev.51aes.com/captchaImage",
            "login_url": "http://oauth-dev.51aes.com/login",
            "login_oauth_url": "http://oauth-dev.51aes.com/oauth/token?grant_type=authorization_code&client_id=gui_client&client_secret=XswhAJYuK",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "7",
            }
        },
        "test03": {
            "authorize_url": "http://oauth-test03.51aes.com/oauth/authorize?client_id=gui_client&grant_type=authorization_code&response_type=code&redirect_uri=http://wdt-frontend-test03.51vr.local",
            "image_url": "http://oauth-test03.51aes.com/captchaImage",
            "login_url": "http://oauth-test03.51aes.com/login",
            "login_oauth_url": "http://oauth-test03.51aes.com/oauth/token?grant_type=authorization_code&client_id=gui_client&client_secret=XswhAJYuK",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "9",
            }
        },
        "stag": {
            "authorize_url": "https://oauth-staging.51aes.com/oauth/authorize?client_id=gui_client&grant_type=authorization_code&response_type=code&redirect_uri=https://gui-frontend-staging.51aes.com",
            "image_url": "https://oauth-staging.51aes.com/captchaImage",
            "login_url": "https://oauth-staging.51aes.com/login",
            "login_oauth_url": "https://oauth-staging.51aes.com/oauth/token?grant_type=authorization_code&client_id=gui_client&client_secret=XswhAJYuK",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "3",
            }
        },
        "release": {
            "authorize_url": "https://oauth.51aes.com/oauth/authorize?client_id=pass_cloud&grant_type=authorization_code&client_secret=XeohHBZxay&response_type=code&redirect_uri=https://paas.51aes.com",
            "image_url": "https://oauth.51aes.com/captchaImage",
            "login_url": "https://oauth.51aes.com/login",
            "login_oauth_url": "https://oauth.51aes.com/oauth/token?grant_type=authorization_code&client_id=pass_cloud&client_secret=XeohHBZxay",
            "redis": {
                "host": "ecp-wdp-redis.redis.rds.aliyuncs.com",
                "password": "test_redis:m2VTawoFfl4NtVdr",
                "port": "6379",
                "db": "1",
            }
        },
        "autotest": {
            "authorize_url": "http://10.100.10.174:30102/oauth/authorize?client_id=gui_client&grant_type=authorization_code&response_type=code&redirect_uri=http://10.100.10.174:30152",
            "image_url": "http://10.100.10.174:30102/captchaImage?lang=en_US",
            "login_url": "http://10.100.10.174:30102/login",
            "login_oauth_url": "http://10.100.10.174:30102/oauth/token?grant_type=authorization_code&client_id=gui_client&client_secret=DnHZZaYXoXi54",
            "redis": {
                "host": "10.100.10.174",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "31106",
                "db": "7",
            }
        }
    },
    "WDP5": {
        "release": {
            "authorize_url": "https://oauth.51aes.com/oauth/authorize?client_id=wdp5-cloud&grant_type=authorization_code&response_type=code&redirect_uri=https://dtp.51aes.com/",
            "image_url": "https://oauth.51aes.com/captchaImage",
            "login_url": "https://oauth.51aes.com/login",
            "login_oauth_url": "https://dtp.51aes.com/api/v1/login/oauth",
            "redis": {
                "host": "10.22.0.9",
                "password": "EcLiJfJMJDbD00QoPEj4",
                "port": "6379",
                "db": "6",
            }
        },
        "test04": {
            "authorize_url": "https://oauth-dev.51aes.com/oauth/authorize?client_id=wdp5_paas_cloud&grant_type=authorization_code&response_type=code&redirect_uri=http://dtp-test04.51vr.local/",
            "image_url": "https://oauth-dev.51aes.com/captchaImage?lang=en_US",
            "login_url": "https://oauth-dev.51aes.com/login",
            "login_oauth_url": "http://dtp-test04.51vr.local/api/v1/login/oauth",
            "redis": {
                "host": "10.100.10.110",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "58128",
                "db": "6",
            }
        }
    },
    "DaaS": {
        "test04": {
            "authorize_url": "https://oauth-dev.51aes.com/oauth/authorize?client_id=daas_client&grant_type=authorization_code&response_type=code&redirect_uri=http://daas-test04.51vr.local/",
            "image_url": "https://oauth-dev.51aes.com/captchaImage?lang=en_US",
            "login_url": "https://oauth-dev.51aes.com/login",
            "login_oauth_url": "http://daas-test04.51vr.local/api/v1/daas/oauth/login",
            "redis": {
                "host": "10.100.10.110",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "58128",
                "db": "6",
            }
        },
        "prv": {
            "authorize_url": "http://10.66.8.165:30062/oauth/authorize?client_id=private-daas-client&grant_type=authorization_code&response_type=code&redirect_uri=http://10.66.8.165:30054/",
            "image_url": "http://10.66.8.165:30062/captchaImage?lang=en_US",
            "login_url": "http://10.66.8.165:30062/login",
            "login_oauth_url": "http://10.66.8.165:30041/api/v1/daas/oauth/login",
            "redis": {
                "host": "10.66.8.165",
                "password": "dzyxDWTMlfjbtPxQBMOYzTlAu0MI3s9x",
                "port": "30033",
                "db": "4",
            }
        }
    }
}

REDIS_CONF = {
    "host": "10.100.20.50",
    "password": None,
    "port": "6379",
    "db": "9",
}

PROJECTS = ['PAAS', 'MEET', 'GUI', 'WDP5', "DaaS"]
