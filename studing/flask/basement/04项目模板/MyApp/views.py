from flask import Blueprint, render_template

#创建蓝图
blue = Blueprint('user', __name__)
# 定义执行函数
@blue.route('/')
def Home():
    data = {
        'name': 'zhangjiang',
        'company': 'tencent',
        'hobbies': ['coding','reading','visiting']
    }
    return render_template('home.html',**data)
