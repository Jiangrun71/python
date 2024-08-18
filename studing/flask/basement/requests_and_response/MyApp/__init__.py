# 初始化文件, 创建flask文件
from flask import Flask #导入包
from .views import blue

def create_app():
    app = Flask(__name__) #创建应用

    #主从蓝图
    app.register_blueprint(blueprint=blue)
    return app