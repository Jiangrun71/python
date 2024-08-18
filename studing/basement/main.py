# # 打印字面量
# print("Hello World")
# print(666)
# print(13.14)
#
# # 类型  整数 浮点数 字符串
#
# """
# 这是一个多行注释
# 这是另外一行
# 首尾用三个双引号
# 多行注释一般写在开头位置
# """
#
# # 变量
# # 变量名称 = 变量值
# money = 50
# print("钱包还有:", money)
# # 变量运算
# # 买了10元蛋糕，还剩多少钱
# # money = money - 10
# # action = "买蛋糕"
# # print(action)
# # print(action,"之后还剩", money, "元")
# # print("我是","张江")
# # print("我是""，张江")
# # print("woshi "+"zhangjain")
# # tel = 128929
# # print("我的电话是：",tel)
# # # 字符串格式化
# # # 字符串拼接
# #
# # name = "Zhangjiang"
# # age = 29
# # money = 200.99
# # message = "我的名字是：%s,我的年纪是：%d,我的余额是：%5.2f" %(name, age, money)
# # print(message)
# #
# # name = "疏文慧"
# # age = 25
# # weight = 120.28
# # print(f"我的名字是{name},我今年已经{age}岁,我的体重是{weight}斤")
#
# # 输入 循环 判断
# # i = 0
# # while i < 3:
# #     print("我想知道你的名字，请在下方输入你的名字：")
# #     name = input("和单独pint打印的效果一样：")
# #
# #     if name == "疏文慧":
# #         print("ok，我知道了，你的名字是%s ,你就是我最喜欢的那个人" % name)
# #     else:
# #         print("ok，我知道了，你的名字是%s " % name)
# #     i += 1
#
# # 判断语句
# des = "itheima is a brand of itcast"
# count = 0
# for i in des:
#     if i == "a":
#         count += 1
# print(f"{des}中共有{count}个a")
#
# # 学习案例
# import random
# salary = 10000
# people = 0
# for i in range(1,21):
#     num = random.randint(1, 10)
#     if num < 5:
#         print(f"员工编号{i},绩效分是{num},低于5分，不发工资，下一位...")
#         continue
#     else:
#         print(f"向员工{i}绩效分是{num},给与发放工资1000元")
#         salary -= 1000
#         print(f"公司账户余额是：{salary}")
#         people += 1
#     if 0 == salary:
#         print(f"工资全部发完了，其他人下个月再领吧！")
#         print(f"一共给{people}个人发了工资")
#         break
#






