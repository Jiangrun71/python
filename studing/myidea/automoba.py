# 读取输入的整数个数 N
N = int(input().strip())

# 读取 N 个随机整数并存储在列表中
random_numbers = []
for _ in range(N):
    num = int(input().strip())
    random_numbers.append(num)

# 使用集合去除重复元素，然后转换为排序后的列表
unique_numbers = sorted(set(random_numbers))

# 输出排序后的唯一整数
for num in unique_numbers:
    print(num)
