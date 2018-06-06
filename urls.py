#coding=utf-8

from handlers import HeFei
from tornado.web import url
import os

handlers = [
     (r"/api/hefei/list", HeFei.HeFeiListHandler), # 城市合肥的列表数据
     # (r'/(.*)', BaseHandler.StaticFileBaseHandler, dict(path=os.path.join(os.path.dirname(__file__), 'template'), default_filename='index.html')),
]