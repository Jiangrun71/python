import sys
import platform
from tkinter.messagebox import *
showwarning(title='提示',message='欢迎光临')
print(platform.platform())
print(sys.platform)
print(sys.path)
class Person:
    def sayhello(self):
        print("hello")
p = Person()
p.sayhello()
