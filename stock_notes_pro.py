# coding: utf-8
import os
from app import create_app, db
from app.models import User
from flask_cors import *
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# @app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
# 定义后端的端口和服务ip段
server = Server(host="0.0.0.0", port=8888)
manager.add_command('runserver',server)
# 通过flask_cors处理flask的跨域问题
CORS(app, supports_credentials=True)


if __name__ == '__main__':
    manager.run()
