# coding:utf-8

import functools

from utils.session import Session
from utils.response_code import RET, error_map


def required_login(fun):
    # 保证被装饰的函数对象的__name__不变
    @functools.wraps(fun)
    def wrapper(request_handler_obj, *args, **kwargs):
        # 调用get_current_user方法判断用户是否登录
        if not request_handler_obj.get_current_user():
        # session = Session(request_handler_obj)
        # if not session.data:
            request_handler_obj.write(dict(errcode=RET.SESSIONERR, errmsg="用户未登录"))
        else:
            fun(request_handler_obj, *args, **kwargs)
    return wrapper

def buildSuccJson(data, **kwargs):
    ret = dict(errcode=RET.OK, errmsg="OK", data=data, **kwargs)
    return ret

def buildFailJson(errcode, errmsg=None):
    if  not errmsg:
        if errcode in error_map:
            errmsg = error_map.get(errcode)
        else:
            errmsg = error_map[RET.UNKOWNERR]
    ret = dict(errcode=errcode, errmsg=errmsg)
    return ret

if __name__ == '__main__':
    print 'test buildSuccJson'
    data = {'key1':'value1', 'key2':'value2'}
    ret = buildSuccJson(data)
    print 'ret1', ret

    data = "{'key1': 'value1', 'key2': 'value2'}"
    ret = buildSuccJson(data)
    print 'ret2', ret

    print 'test buildFailJson'
    errcode = RET.DATAEXIST
    errmsg = 'data error'
    ret = buildFailJson(errcode, errmsg)
    print 'ret1', ret

    errcode = RET.DATAEXIST
    errmsg = None
    ret = buildFailJson(errcode, errmsg)
    print 'ret2', ret

    errcode = 111
    errmsg = 'data error'
    ret = buildFailJson(errcode, errmsg)
    print 'ret3', ret

    errcode = 222
    errmsg = None
    ret = buildFailJson(errcode, errmsg)
    print 'ret4', ret























