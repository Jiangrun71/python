# words = input("请输入想要测试的字符串：").split(" ")

# print(len(words[-1]))
"""
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
输入：
ABCabc
A

输出：
2
"""

# input_str = input()
# input_char = input()
# count = 0
# for char in input_str:
#     if char.lower() == input_char.lower():
#         count += 1
#         continue
# print(count)

"""
明明生成了
N
N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

数据范围： 
1
≤
n
≤
1000
 
1≤n≤1000  ，输入的数字大小满足 
1
≤
v
a
l
≤
500
 
1≤val≤500 
输入描述：
第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 具体格式可以参考下面的"示例"。
输出描述：
输出多行，表示输入数据处理后的结果
"""
# input_num = int(input())
# num_list = []
# for i in range(input_num):
#     num = int(input())
#     num_list.append(num)
# for j in range(len(num_list)):
#     # 如果当前元素和下一个元素相等，则删除下一个元素
#     while j < len(num_list)-1 and num_list[j] == num_list[j+1]:
#         del num_list[j+1]
# for k in sorted(num_list):
#     print(k)

"""
数据结构
"""
# alist = [1,3,4,6,7]
# alist.reverse()
# alist.append(11)
# for i in alist:
#     print(i)
# #alist.pop()
# print(alist)

# my_dic = {"zhangjiang": "18", "wuhan": "2"}
# acedss =['zhangjiang', 'wuhan']
# for i in acedss:
#     print(my_dic[i])

"""
给定⼀个字符串 s ，找出这样⼀个⼦串：
1. 该⼦串中的任意⼀个字符最多出现 2 次；
2. 该⼦串不包含指定某个字符；
请你找出满⾜该条件的最⻓⼦串的⻓度。
输⼊
第⼀⾏为要求不包含的指定字符，为单个字符，取值范围 [0-9a-zA-Z]
第⼆⾏为字符串 s，每个字符范围 [0-9a-zA-Z] ，⻓度范围 [1,10000]
"""
# s = input()
# string = input()
# string_length = len(string)
# sub_length, left_length, right_lengt= 0, 0,0

# for word in string:
#     if word != s:
#         sub_length += 1
#     else:
#         left_length = sub_length
#         sub_length = 0
#         continue

# print(sub_length)

# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         for i in range(n):
#             return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# climbStair = Solution()
# counts = climbStair.climbStairs(10)
# print(counts)
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
                
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 13))
# input_str = input("请输入一个任意字符串：")
# dirct = {}
# for i in input_str:
#     dirct[i] = input_str.count(i)
# print(dirct)

# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         res = []
#         for i in range(max(len(word1), len(word2))):
#             if i < len(word1):
#                 res.append(word1[i])
#             if i < len(word2):
#                 res.append(word2[i])
        
#         return "".join(res)
# sol = Solution()
# print(sol.mergeAlternately('abcd123', 'efgh'))
'''
对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。

给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。

 

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""
'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # 辅助函数，判断 s 是否能由 t 重复多次组成
        def canDivide(s, t):
            return s == t * (len(s) // len(t))
        
        # 获取两个字符串长度的最大公约数
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # 获取 str1 和 str2 长度的最大公约数
        gcd_len = gcd(len(str1), len(str2))
        
        # 截取 str1 的前 gcd_len 个字符，作为可能的公共除数
        candidate = str1[:gcd_len]
        
        # 判断这个公共除数是否能整除 str1 和 str2
        if canDivide(str1, candidate) and canDivide(str2, candidate):
            return candidate
        else:
            return ""

# 测试用例
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # 输出："ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # 输出："AB"
print(solution.gcdOfStrings("ABCDABCD", "BCD"))    # 输出：""








