ca_english_name = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

name_array = []

while True:
    name = input("请输入您的姓名进行登录：")

    if name not in name_array:
        name_array.append(name)
        print("认证成功，欢迎首次登录。")

    else:
        print("你的名字已经注册过，请换一个名字进行登录。")
        continue  # 如果名字已注册，重新循环进行登录

    while True:
        tip = input("请输入要查询的月份，以数字标识（1-12）：")
        try:
            tip = int(tip)
            if 1 <= tip <= 12:
                print(ca_english_name[tip - 1])
            else:
                print("请输入正确的数字（1-12）！")
                continue  # 如果输入不在1-12之间，重新循环要求输入
        except ValueError:
            print("请输入一个有效的整数！")
            continue  # 如果输入无法转换为整数，重新循环要求输入

        continueornot = input("是否继续查询？（回复 'yes' 或 'no'）：")
        if continueornot.lower() != 'yes':
            break  # 如果不继续查询，退出内部循环

    exitornot = input("是否退出程序？（回复 'yes' 或 'no'）：")
    if exitornot.lower() == 'yes':
        print("程序已退出。")
        break  # 如果退出程序，退出外部循环
