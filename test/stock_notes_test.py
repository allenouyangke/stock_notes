# -*- coding: utf-8 -*-
from flask import Flask, render_template
import tushare as ts
import pandas as pd
from flask_cors import *
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
CORS(app, supports_credentials=True)

# 多个股票查询
@app.route('/', methods=['POST','GET'])
@app.route('/todo/api/v1.0/tasks', methods=['POST', 'GET'])
def meg():
    stock_num = ['601601', '600519', '002039', '000568', '600236']
    stock_list = []
    for code in stock_num:
        df = ts.get_k_data(code, ktype='5')
        df = df.iloc[[-1]]
        stock_list.append(df)
    stock_pd = pd.concat(stock_list)
    return stock_pd.to_json(orient='records')

# 单支股票数据进行查询
@app.route('/todo/api/v1.0/tasks/<code>', methods=['POST','GET'])
def meg_single(code):
    codes = str(code)
    stock_list = []
    df = ts.get_k_data(codes, ktype='5')
    df = df.iloc[[-1]]
    stock_list.append(df)
    stock_pd = pd.concat(stock_list)
    return stock_pd.to_json(orient='records')

    # 定义错误页面404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 定义错误页面500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
  # 通过flask_cors处理flask的跨域问题
  # app.run(host="0.0.0.0", port=8888, debug=True)
  manager.run()

