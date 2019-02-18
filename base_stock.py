# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column, String, Integer
# 引入需要的模块
from sqlalchemy.ext.declarative import declarative_base

import tushare as ts
import pandas

ts.set_token('cdfe3ce3a8717b588f35f80a39d239ea4f56e224fd6163d4a3568e4b')
pro = ts.pro_api()

# 创建基础类
BaseModel = declarative_base()

# 创建一个和mysql数据库之间的连接引擎对象
engine = create_engine("mysql://root:123456@127.0.0.1/stock_note?charset=utf8", encoding="utf-8", echo=True)
# 创建一个连接会话对象；需要指定是和那个数据库引擎之间的会话
# Session = sessionmaker(bind=engine)
# session = Session()
# 接下来~就可以用过session会话进行数据库的数据操作了。

# 初始化，获取tushare的basic stock，并入库，方便前端进行查询搜索
def base_init():
    print 'start to init base stock ............'
    data = pro.stock_basic(fields='ts_code,symbol,name,area,industry,market,list_date')
    data.to_sql('base_stock',engine,if_exists='append',index=False)
    print 'init base stock success !!............'

if __name__ == "__main__":
    Base.metadata.create_all()
    baseinit()

