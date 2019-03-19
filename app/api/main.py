# -*- coding: utf-8 -*-
from flask import request
from flask import jsonify
from flask_restful import reqparse
from . import api
import json

import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("127.0.0.1", "root", "123456", "stock_note", charset='utf8')
# 使用cursor()方法获取操作游标 
cursor = db.cursor(MySQLdb.cursors.DictCursor)


@api.route('/api/v1/<table_name>/<action>',methods=['POST'])
def parse_request(table_name,action):
    print 'it is arrive here'
    print "table_name:  %s " % table_name
    print "action:  %s " % action
    print type(request.data)

    # 前端传参需要预处理，空参数需要预设个固定变量，再传给处理函数
    if request.data is '':
        parser = None
    else:
        parser = request.get_json()
    
    # 将前端参数提交处理函数
    if (action == 'read'):
        result = read(table_name,parser)

    if (action == 'create'):
        return create(table_name,parser)
        
    # 回调前端   
    result = respose(result)
    return jsonify(result)

# 回调前端
def respose(data):
    res = {"data":data}
    return res

# 数据库操作  <读>
def read(table_name,parser=None):
    if parser is None:
        parser = {}
        parser['limit'] = 5
    limit = parser['limit']
    print "limit: %s" % limit
    cursor.execute('select * from %s limit %s' % (table_name,limit))
    results = cursor.fetchall()
    print results
    return results

# 数据库操作 <写>
def create(table_name,parser):
    print type(parser)
    key = parser.keys()
    val = parser.values()
    
    # 处理key、value便于拼接insert语句
    key = ','.join(key)
    val = json.dumps(val)
    val = val.decode('unicode_escape')
    val = val.lstrip('[')
    val = val.rstrip(']')
    print val

    sql = "insert into %s(%s) values (% s)" % (table_name,key, val)
    
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        result = {"status":"success"}
        return result
    except:
        # Rollback in case there is any error
        db.rollback()
        result = {"status":"fail"}
        return result