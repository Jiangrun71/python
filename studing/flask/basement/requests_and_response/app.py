# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World! ZhangJiang2! welcome to python!'
#
#
# if __name__ == '__main__':
#     app.run(debug=True,port=5000)
from MyApp import create_app
app = create_app()

#定义路由


#启动服务
if __name__ == '__main__':
    app.run(debug=True)