#coding=utf-8

from handlers import HeFei
from handlers import Register
from tornado.web import url
import os

handlers = [
     (r"/api/hefei/list", HeFei.HeFeiListHandler), # 城市合肥的列表数据
     (r"/api/hefei/getdetail", HeFei.GetDetailHandler), # 城市合肥的详情数据
     (r"/api/jregister", Register.RegisterUserHandler), # 金融注册
     # (r'/(.*)', BaseHandler.StaticFileBaseHandler, dict(path=os.path.join(os.path.dirname(__file__), 'template'), default_filename='index.html')),
]