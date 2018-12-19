# coding: utf-8
import tushare as ts
import pandas as pd
import json
from flask import request
from datetime import timedelta, datetime
from . import main


#设置ts的token
ts.set_token('cdfe3ce3a8717b588f35f80a39d239ea4f56e224fd6163d4a3568e4b')
pro = ts.pro_api()

#获取当前日期
d=datetime.now() #获取当前周几，如果是周末需要往前获取周五的日期
if (d.weekday() == 6):
    today = (datetime.today() + timedelta(-2)).strftime('%Y%m%d')
elif (d.weekday() == 5):
    today = (datetime.today() + timedelta(-1)).strftime('%Y%m%d')
elif (d.hour <= 15 ):
    today = (datetime.today() + timedelta(-1)).strftime('%Y%m%d')  
else:
    today = datetime.today().strftime('%Y%m%d')

@main.route('/todo/api/v1.0/tasks', methods=['POST'])
def meg():
    data = request.data
    j_data = json.loads(data)
    print type(j_data)
    stock_num = j_data
    print stock_num
    print today
    stock_list = []
    for code in stock_num:
        # df= ts.get_k_data(code, ktype='5')
        code = code.encode('ascii','ignore')
        if (code.startswith('6')):
            code = code + '.SH'
        else:
            code = code + '.SZ'
        df = pro.daily(ts_code=code, trade_date=today)
        print df
        df= df.iloc[[-1]]
        stock_list.append(df)
    stock_pd = pd.concat(stock_list)
    return stock_pd.to_json(orient='records')


@main.route('/', methods=['POST', 'GET'])
@main.route('/todotest/api/v1.0/tasks', methods=['POST', 'GET'])
def meg_test():
    stock_num = ['601601', '600519', '002039', '000568', '600236']
    stock_list = []
    for code in stock_num:
        df = ts.get_k_data(code, ktype='5')
        df = df.iloc[[-1]]
        stock_list.append(df)
    stock_pd = pd.concat(stock_list)
    return stock_pd.to_json(orient='records')

@main.route('/todo/api/v1.0/tasks/<code>', methods=['POST','GET'])
def meg_single(code):
    codes = str(code)
    stock_list = []
    df = ts.get_k_data(codes, ktype='5')
    df = df.iloc[[-1]]
    stock_list.append(df)
    stock_pd = pd.concat(stock_list)
    return stock_pd.to_json(orient='records')
