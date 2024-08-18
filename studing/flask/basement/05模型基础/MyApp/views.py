from flask import Blueprint

#创建蓝图
blue = Blueprint('user', __name__)
# 定义执行函数
@blue.route('/')
def hello():
    return "this is my website"