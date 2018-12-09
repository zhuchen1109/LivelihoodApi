# coding:utf-8

import logging
import json
import datetime

from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.commons import buildSuccJson, buildFailJson

class RegisterUserHandler(BaseHandler):

    def post(self):
        '''
        需要参数cardId
        :return:返回指定的详情页数据
        '''

        # 姓名
        name = self.get_argument('name', None)
        # 年龄
        age = self.get_argument('age', None)
        # 手机号
        phone = self.get_argument('phone', None)
        # 微信号
        wechat = self.get_argument('wechat', None)
        # 芝麻分
        score = self.get_argument('score', None)
        # 银行卡号
        bankNum = self.get_argument('bankNum', None)
        # 银行地址
        bank = self.get_argument('bank', None)
        # 身份证号
        card = self.get_argument('card', None)
        # 地址
        address = self.get_argument('address', None)
        # 配偶
        wife = self.get_argument('wife', None)
        # 配偶电话
        wifePhone = self.get_argument('wifePhone', None)
        # 父亲
        father = self.get_argument('father', None)
        # 父亲电话
        fatherPhone = self.get_argument('fatherPhone', None)
        # 母亲
        mother = self.get_argument('mother', None)
        # 母亲电话
        motherPhone = self.get_argument('motherPhone', None)
        # 同事
        workmate = self.get_argument('workmate', None)
        # 同事电话
        workmatePhone = self.get_argument('workmatePhone', None)
        # 朋友
        friend = self.get_argument('friend', None)
        # 朋友电话
        friendPhone = self.get_argument('friendPhone', None)
        # 公司名称
        workUnit = self.get_argument('workUnit', None)
        # 职位
        work = self.get_argument('work', None)
        # 单位电话
        unitPhone = self.get_argument('unitPhone', None)
        # 单位地址
        workAddress = self.get_argument('workAddress', None)
        # 社保
        socialSecurity = self.get_argument('socialSecurity', None)
        # 注册时间
        #createTime = models.DateTimeField(auto_now_add=True)
        # 更新时间
        #updateTime = models.DateTimeField(auto_now=True)

        #sql = "select cardId,title,type,source,reply,hotCount,replyDate,createTime,content,replyContent from ll_card_detail where cardId=%(cardId)s;"
        sql = "insert into register_user (name, age, phone, wechat, score, bankNum, bank, card, address, wife, wifePhone, father, fatherPhone, mother, motherPhone, workmate, workmatePhone, friend, friendPhone, workUnit, work, unitPhone, workAddress, socialSecurity, createTime, updateTime) " \
              "values (%(name)s, %(age)s, %(phone)s, %(wechat)s, %(score)s, %(bankNum)s, %(bank)s, %(card)s, %(address)s, %(wife)s, %(wifePhone)s, %(father)s, %(fatherPhone)s, %(mother)s, %(motherPhone)s, %(workmate)s, %(workmatePhone)s, %(friend)s, %(friendPhone)s, %(workUnit)s, %(work)s, %(unitPhone)s, %(workAddress)s, %(socialSecurity)s, %(createTime)s, %(updateTime)s);"
        sql_params = {}
        sql_params['name'] = name
        sql_params['age'] = age
        sql_params['phone'] = phone
        sql_params['wechat'] = wechat
        sql_params['score'] = score
        sql_params['bankNum'] = bankNum
        sql_params['bank'] = bank
        sql_params['card'] = card
        sql_params['address'] = address
        sql_params['wife'] = wife
        sql_params['wifePhone'] = wifePhone
        sql_params['father'] = father
        sql_params['fatherPhone'] = fatherPhone
        sql_params['mother'] = mother
        sql_params['motherPhone'] = motherPhone
        sql_params['workmate'] = workmate
        sql_params['workmatePhone'] = workmatePhone
        sql_params['friend'] = friend
        sql_params['friendPhone'] = friendPhone
        sql_params['workUnit'] = workUnit
        sql_params['work'] = work
        sql_params['unitPhone'] = unitPhone
        sql_params['workAddress'] = workAddress
        sql_params['socialSecurity'] = socialSecurity
        sql_params['createTime'] = datetime.datetime.now()
        sql_params['updateTime'] = datetime.datetime.now()

        try:
            ret = self.db.insert(sql, **sql_params)
        except Exception as e:
            logging.error(e)
            return self.write(buildFailJson(RET.DATAERR, '数据库插入出错'))

        if not ret:
            return self.write(buildFailJson(RET.SERVERERR))

        retData = json.dumps(buildSuccJson(data="注册成功"))
        return self.write(retData)










