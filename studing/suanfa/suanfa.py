# 定义一个Person类
class Person:
# 构造函数
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# 定义一个方法，用于打印个人信息

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my email is {self.email}.")

# 创建一个Person实例 person , 并传入三个参数 "Alice", 30, "alice@example.com"
person = Person("Alice", 30, "alice@example.com")

# 调用方法
person.introduce() 
def process_person(person):
    print(f"Processing person: {person.name}")
    if person.age > 18:
        print("Age is greater than 18.")
    else:
        print("Age is less than or equal to 18.")
    print(f"Email: {person.email}")

# 创建Person实例
person = Person("Bob", 25, "bob@example.com")

# 将Person实例作为参数传递给函数
process_person(person)