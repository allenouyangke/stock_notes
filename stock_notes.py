# -*- coding: utf-8 -*-
from flask import Flask
import tushare as ts
import pandas as pd
import json
from datetime import timedelta, datetime
from flask_cors import *
from flask import request
from flask_script import Manager,Server


app = Flask(__name__)
manager = Manager(app)
server = Server(host="0.0.0.0", port=8888)
manager.add_command('runserver',server)
# 通过flask_cors处理flask的跨域问题
CORS(app, supports_credentials=True)

#设置ts的token
ts.set_token('cdfe3ce3a8717b588f35f80a39d239ea4f56e224fd6163d4a3568e4b')
pro = ts.pro_api()

#获取当前日期
d=datetime.now() #获取当前周几，如果是周末需要往前获取周五的日期
if (d.weekday() == 6):
    today = (datetime.today() + timedelta(-2)).strftime('%Y%m%d')
elif (d.weekday() == 5):
    today = (datetime.today() + timedelta(-1)).strftime('%Y%m%d')
else:
    today = datetime.today().strftime('%Y%m%d')


@app.route('/todo/api/v1.0/tasks', methods=['POST','GET'])
def meg():
    data = request.data
    j_data = json.loads(data)
    print type(j_data)
    stock_num = j_data
    #stock_num = ['000001']
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

if __name__ == '__main__':
  # app.run(host="0.0.0.0", port=8888, debug=True
    manager.run()
