# coding:utf-8

PIC_CODE_EXPIRES_SECONDS = 180 # 图片验证码的有效期，单位秒
SMS_CODE_EXPIRES_SECONDS = 300 # 短信验证码的有效期，单位秒

SESSION_EXPIRES_SECONDS = 86400 # session数据有效期， 单位秒

QINIU_URL_PREFIX = "http://o91qujnqh.bkt.clouddn.com/" # 七牛存储空间的域名

CARD_LIST_PAGE_CAPACITY = 20 # 列表页每页显示数目
CARD_LIST_PAGE_CACHE_NUM = 2 # 房源列表页每次缓存页面书

REDIS_KEY_HF_LIST = 'hefei_list'
REDIS_KEY_HF_TOTAL_PAGE = 'hefei_total_page'
REDIS_CARD_LIST_EXPIRES_SECONDS = 600 # 列表页数据缓存时间 秒