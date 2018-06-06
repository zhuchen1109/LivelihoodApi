#coding=utf-8

import os


# Applicaton config
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'cookie_secret': 'b+t4dMZLTiagmie2YqhhPisIwNqR9kpVtowiC4sw3lM=',
    'xsrf_cookies': True,
    'debug':True,
}

# mysql
mysql_option = dict(
    host='127.0.0.1',
    database='livelihood',
    user='root',
    password='root'
)

#redis
redis_option = dict(
    host='127.0.0.1',
    port=6379
)

#log file
log_file = os.path.join(os.path.dirname(__file__), 'logs/log')
log_level = 'debug'

sessin_expires = 86400 # session有效期 单位秒

# 密码加密密钥
passwd_hash_key = 'nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ='