# scopes1.py
# 局部和全局作用域的比较
# 定义了一个称为local的函数
def local():
    m = 7
    print(m)
# 在全局作用域中定义了m
m = 5
# 调用（或执行）local函数
local()
print(m)
