# coding:utf-8

import logging
import json
import math
import constants

from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.commons import buildSuccJson, buildFailJson

class HeFeiListHandler(BaseHandler):
    """分页返回合肥列表数据"""
    def get(self):
        '''
        传入参数说明：
        page      数据页数  非必须  默认值：1
        :return:返回第page页，共pagesize条数据
        '''
        page = self.get_argument('page', '1')
        if not page.isdigit():
            logging.debug('传入的page不是数字，page:%s' % page)
            return self.write(buildFailJson(RET.PARAMERR, '参数page只能传入有效数字'))
        page = int(page)
        if int(page) <= 0:
            logging.debug('传入的page非法，page:%s' % page)
            page = 1

        total_page = -1;
        # 在redis中查询列表总页数
        try:
            ret = self.redis.get(constants.REDIS_KEY_HF_TOTAL_PAGE)
        except Exception as e:
            logging.error(e)
            ret = None
        if ret:
            if not isinstance(ret, int):
                total_page = int(ret)
            else:
                total_page = ret
            logging.info('hit redis %s:%s' % (constants.REDIS_KEY_HF_TOTAL_PAGE, total_page))

        # 在redis未查到，去数据库获取
        if total_page == -1:
            logging.debug('执行数据库查询页数')
            sql_count = 'select count(1) as count from ll_card_detail'
            try:
                ret = self.db.get(sql_count)
            except Exception as e:
                logging.warn(e)
                return self.write(buildFailJson(RET.DBERR, "数据库查询出错"))
            else:
                total_page = int(math.ceil(ret['count'] / float(constants.CARD_LIST_PAGE_CAPACITY)))
                self.redis.set(constants.REDIS_KEY_HF_TOTAL_PAGE, total_page, ex=constants.REDIS_CARD_LIST_EXPIRES_SECONDS)
                # self.redis.expire(constants.REDIS_KEY_HF_TOTAL_PAGE, constants.REDIS_CARD_LIST_EXPIRES_SECONDS)
                if page > total_page:
                    return buildSuccJson(data=[], total_page=total_page)

        # 先到redis中查询数据，如果获取到了数据，直接返回给用户
        try:
            ret = self.redis.hget(constants.REDIS_KEY_HF_LIST, page)
        except Exception as e:
            logging.error(e)
            ret = None
        if ret:
            # 此时从redis中读取到的数据ret是json格式字符串
            logging.info("hit redis: %s,page:%s" % (constants.REDIS_KEY_HF_LIST, page))
            return self.write(ret)

        # 查询Mysql数据库，获取列表数据
        # 分页
        # limit 10 返回前10条
        # limit 20,3 从20条开始，返回3条数据
        logging.debug('执行数据库查询列表数据，page:%s' % page)
        sql = "select cardId,title,type,source,reply,replyDate from ll_card_detail order by replyDate desc"
        if 1 == page:
            sql += " limit %s" % (constants.CARD_LIST_PAGE_CAPACITY * constants.CARD_LIST_PAGE_CACHE_NUM)
        else:
            sql += " limit %s,%s" % ((page - 1) * constants.CARD_LIST_PAGE_CAPACITY,
                                     constants.CARD_LIST_PAGE_CAPACITY * constants.CARD_LIST_PAGE_CACHE_NUM)
        try:
            ret = self.db.query(sql)
        except Exception as e:
            logging.error(e)
            return self.write(buildFailJson(RET.DBERR, "数据库查询出错"))
        if not ret:
            return self.write(buildFailJson(RET.NODATA, "没有数据"))
        # json转对象
        data = []
        for row in ret:
            d = {
                "cardId": row.get("cardId", ""),
                "title": row.get("title", ""),
                "type": row.get("type", 0),
                "source": row.get("source", ""),
                "reply": row.get("reply", ""),
                # "replyDate": row.get("replyDate", None),
            }
            replyDate = row.get("replyDate", None)
            if not replyDate:
                d['replyDate'] = replyDate.strftime('%Y-%m-%d')
            data.append(d)
        # 对与返回的多页面数据进行分页处理
        # 首先取出用户想要获取的page页的数据
        current_page_data = data[:constants.CARD_LIST_PAGE_CAPACITY]
        datas = {}
        datas[page] = json.dumps(buildSuccJson(current_page_data, total_page=total_page))
        # 将多取出来的数据分页
        i = 1
        while 1:
            page_data = data[i * constants.CARD_LIST_PAGE_CAPACITY: (i + 1) * constants.CARD_LIST_PAGE_CAPACITY]
            if not page_data:
                break
            datas[page + i] = json.dumps(buildSuccJson(current_page_data, total_page=total_page))
            i += 1
        try:
            redis_key = constants.REDIS_KEY_HF_LIST
            self.redis.hmset(redis_key, datas)
            self.redis.expire(redis_key, constants.REDIS_CARD_LIST_EXPIRES_SECONDS)
        except Exception as e:
            logging.error(e)

        return self.write(datas[page])

















