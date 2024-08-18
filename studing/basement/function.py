def say_hi(name):
    print(f"你好,{name}")
say_hi("zhangjiang")


students = ["zhangsan","lisi","wangwu"]
print(students)
print(students[1])
#访问列表最后一个元素
print(students[-1])
students[0] = "zhanghe"
#末尾追加元素
students.append('wangliu')
print(students)
#指定位置插入元素
students.insert(1,"libai")
print(students)
#删除指定位置元素
del students[1]
print(students)
#弹出元素
students_poped = students.pop()
print(students_poped)

students_poped = students.pop(1)
print(students_poped)
print(students)
#根据值删除元素
students.remove('zhanghe')
print(students)

#元素排序
students = ["zhangsan","lisi","wangwu"]
students.sort()
print(students)
students.sort(reverse=True)
print(students)

#使用sorted 临时排序
print(sorted(students))

#倒着打印列表
students.reverse()
print(students)
print(len(students))

#第四章 操作列表
#4.1 遍历整个列表
for student in students:
    print(student)

#第八章 函数
# 函数的定义
def greerer (username):
    print("这是函数体")
    print("hello",username)
greerer("zhangjiang")

#类方法和实例方法

#文件和异常
file_path = "C:\\Users\\Zhang\\Desktop\\test.txt"
with open(file_path,'r+') as file_object:
    contents = file_object.read()
    print(contents)
    contents = file_object.write("add a new line")
    contents = file_object.read()
    print(contents)

