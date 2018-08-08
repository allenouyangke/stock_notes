# -*- coding: utf-8 -*-
from flask import Flask
import tushare as ts
import pandas as pd
import json
from flask_cors import *
from flask import request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
# 通过flask_cors处理flask的跨域问题
CORS(app, supports_credentials=True)

@app.route('/todo/api/v1.0/tasks', methods=['POST','GET'])
def meg():
    data = request.data
    j_data = json.loads(data)
    print type(j_data)
    stock_num = j_data
    #stock_num = ['000001']
    stock_list = []
    for code in stock_num:
        df= ts.get_k_data(code, ktype='5')
        df= df.iloc[[-1]]
        stock_list.append(df)
    stock_pd = pd.concat(stock_list)
    return stock_pd.to_json(orient='records')

if __name__ == '__main__':
  # app.run(host="0.0.0.0", port=8888, debug=True
    manager.run()

