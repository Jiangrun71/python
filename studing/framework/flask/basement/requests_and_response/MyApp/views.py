from flask import Blueprint, request, render_template, make_response, Response, redirect, url_for

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

@blue.route('/methods/', methods=['GET', 'POST'])
def mymethods():
    return "this is my methods"

#请求和响应
# http: 一次前后端交互：先请求再响应

@blue.route('/request/', methods=['POST', 'GET'])
def get_myrequest():
   # print(request)

    print(request.method) #请求方法
    #get请求参数
    # print(request.args)
    # print(request.args['name']), request.args['age']
    # print(request.args.get('name'))
    # print(request.args.getlist('name'))
    print(request.form)
    print(request.form.get('name'))
    print(request.user_agent)
    return 'request ok!'

# response
@blue.route('/response/', methods = ['POST','GET'])
def my_response():
    #响应的几种方式。
    #1、返回字符串（不常用）
    #2、模板渲染
    #return render_template('index.html', name='张江')

    #3、返回json数据（前后端分离）
    # data = {'name': 'lisi'}
    # return data

    # 4、自定义response 对象
    html = render_template('index.html', name='张江')
    print(html, type(html))
    #res = make_response(html, 200)
    res = Response(html)
    return res

# redirect 重定向
@blue.route('/redirect/')
def my_redirect():

    #1、重定向网址
    #return redirect('https://baidu.com')

    #2、嵌入本地路径
    return redirect('/response/')

    #3、url_for('蓝图名称.视图函数名')


