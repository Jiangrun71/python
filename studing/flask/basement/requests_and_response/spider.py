import requests

#get请求
# res = requests.get('http://127.0.0.1:5000/request/?name=lisi&age=29')
# print(res.text)

#post请求

pos = requests.post('http://127.0.0.1:5000/response/', data={'name':'zhangjiang', 'age': 12})
print(pos.text)

