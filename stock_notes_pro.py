# coding: utf-8
import os
from app import create_app
from flask_cors import *
from flask_script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
# 通过flask_cors处理flask的跨域问题
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    manager.run()
