# coding: utf-8
import tushare as ts
import pandas as pd
import json
from flask import request
from . import main


@main.route('/todo/api/v1.0/tasks', methods=['POST', 'GET'])
def meg():
    data = request.data
    j_data = json.loads(data)
    print type(j_data)
    stock_num = j_data
    #stock_num = ['000001']
    stock_list = []
    for code in stock_num:
        df = ts.get_k_data(code, ktype='5')
        df = df.iloc[[-1]]
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
