# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
# 引入需要的模块
from sqlalchemy.ext.declarative import declarative_base

import tushare as ts

ts.set_token('cdfe3ce3a8717b588f35f80a39d239ea4f56e224fd6163d4a3568e4b')
pro = ts.pro_api()

# 创建基础类
BaseModel = declarative_base()

# 创建一个和mysql数据库之间的连接引擎对象
engine = create_engine("mysql://root:123456@127.0.0.1/stock_note", encoding="utf-8", echo=True)
# 创建一个连接会话对象；需要指定是和那个数据库引擎之间的会话
Session = sessionmaker(bind=engine)
session = Session()
# 接下来~就可以用过session会话进行数据库的数据操作了。


class baceStock(BaseModel):
    __tablename__ = "base_stock"
    #创建字段
    ts_code = Column(String,primary_key=True) #ts代码
    symbol = Column(String) #股票代码
    name = Column(String) #股票名称
    area = Column(String) #所在区域
    industry = Column(String) #所在行业
    fullname = Column(String) #股票全称
    enname = Column(String) #英文全称
    market = Column(String) #市场类型 （主板/中小板/创业板）
    exchange = Column(String) #交易所代码
    curr_type = Column(String) #交易货币
    list_status = Column(String) #上市状态： L上市 D退市 P暂停上市
    list_date = Column(String) #上市日期
    delist_date = Column(String) #退市日期
    is_hs = Column(String) #是否沪深港通标的，N否 H沪股通 S深股通

def baseinit():
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_sql('base_stock',ENGINE,if_exists='append')

if __name__ == "__main__":
    Base.metadata.create_all()
    baseinit()

