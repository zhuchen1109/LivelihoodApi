#coding = utf-8

import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import torndb
import redis

from tornado.options import define, options
from urls import handlers
from config import *

define(name='port', default=8000, type=int, help='run server on the given prot')

class Application(tornado.web.Application):

    def __init__(self):
        super(Application, self).__init__(handlers, **settings)
        self.db = torndb.Connection(**mysql_option)
        self.redis = redis.StrictRedis(**redis_option)

def main():
    options.log_file_prefix = log_file
    options.logging = log_level
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()