from flask import Blueprint

#创建蓝图
blue = Blueprint('user', __name__)
# 定义执行函数


@blue.route("/")
def hello():
    print()
    return "this is my website"

# string 重点
@blue.route('/string/<string:username>/')
def get_string(username):
    print()
    return username

@blue.route('/int/<int:id>/')
def get_int(id):
    print()
    return str(id)

@blue.route('/float/<float:weight>/')
def get_weight(weight):
    print()
    return str(weight)

@blue.route('/getuuid')
def get_getuudi():
    print()
    import uuid
    return str(uuid.uuid4())

@blue.route('/any/<any(age, healthy. money):person>/')
def get_any(person):
    print(type(person))
    return str(person)

#methods 请求方法，默认不支持post
#如果需要同时支持GET和POST,就设置methods

@blue.route('/methods/',methods=['GET','POST'])
def mymethods():
    return "this is my methods"


