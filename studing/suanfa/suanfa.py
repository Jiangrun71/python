class Solution:
    def solve(self, s: str, t: str) -> str:
        # 移除字符串中的空格
        s = s.strip()
        t = t.strip()

        # 检查是否至少有一个字符串是有效的整数
        if s.isdigit() or t.isdigit():
            try:
                # 尝试将有效的字符串转换为整数
                num1 = int(s) if s.isdigit() else 0
                num2 = int(t) if t.isdigit() else 0
                # 计算和
                print(num1, num2)
                sum = str(num1 + num2)
                return sum
            except ValueError:
                # 如果转换失败，返回错误信息
                return "Invalid input: One or both strings are not valid integers."
        else:
            # 如果两个字符串都不是有效的整数
            return "Invalid input: Both strings are not valid integers."


# 创建 Solution 类的实例
sol = Solution()

# 测试有效的输入
result = sol.solve("1000003", " 00001 ")
print(result)  # 应该输出 "1010004"

# 测试一个参数为空的情况
result = sol.solve("1000003", " ")
print(result)  # 应该输出 "1000003"

# 测试两个参数都为空的情况
result = sol.solve(" ", " ")
print(result)  # 应该输出 "Invalid input: Both strings are not valid integers."
