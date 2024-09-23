# #split(",") 拆分输入字符串为⼀个列表 input().split(",")
# riddles = input().split(",")
# answers = input().split(",")
# # 初始化结果列表res = []
# res = list()

#  # 构建谜底库answers_dic，其中
#  # key为每⼀个谜底answer去重后排序的结果a
#  # value为每⼀个谜底answer⾃⾝
# # 初始化answers_dic = {}
# # answers_dic = dict()

# # # 遍历每⼀个谜底answer 
# # for answer in answers:
# #     a = "".join(sorted(set(answer))) #  
# #     answers_dic[a] = answer


# # # 遍历每⼀个谜⾯riddle
# # for riddle in riddles:
# # # 得到riddle去重后排序的结果r
# #     r = "".join(sorted(set(riddle)))
# # # 查看r是否位于谜底库中
# # # 若在则将对应的谜底answers_dic[r]加⼊res中
# # # 否则储存字符串"not found"
# #     if r in answers_dic:
# #         res.append(answers_dic[r])
# #     else:
# #         res.append("not found")


# # print(",".join(res))


# # def max_subarray_sum(nums):
# #     if not nums:  # 检查是否为空数组
# #         return 0

# #     current_sum = max_sum = nums[0]
    
# #     for num in nums[1:]:
# #         # 如果当前子序列和为负，则抛弃，重新开始计算
# #         current_sum = max(num, current_sum + num)
# #         # 更新全局最大值
# #         max_sum = max(max_sum, current_sum)
    
# #     return max_sum

# # # 示例使用
# # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# # print("最大连续子序列和:", max_subarray_sum(nums))
# list = []
# list.append(1)
# print(list)

nums = list(map(int, input()[1:-1].split(",")))
target = int(input())
print(nums)

# 初始化索引和最⼩值的取值，这⾥可以取inf，也可以取nums⻓度乘2
min_idx_sum = len(nums)*2
# 构建哈希表，储存每⼀种步数⾸次出现的下标
hash_dic = dict()
# 初始化答案列表
ans = [0, 0]

# 遍历nums
for i, num in enumerate(nums):
# 计算target-num的值rest_num
    rest_num = target-num
# 若rest_num位于哈希表中，说明其曾经出现过
# rest_num和num相加等于所需要的结果target
    if rest_num in hash_dic:
# 若此时min_idx_sum⼤于两者下标和
# 则更新min_idx_sum和ans
        if min_idx_sum > hash_dic[rest_num] + i:
            min_idx_sum = hash_dic[rest_num] + i
# 注意题⽬要求两个元素保持原有顺序
            ans = [rest_num, num]
# 若num不位哈希表中，说明它第⼀次出现，记录其下标
# 由于我们希望两数的下标和尽可能⼩
# 故对于重复出现的数字，只记录其第⼀次出现的下标即可
    if num not in hash_dic:
        hash_dic[num] = i


# 输出答案，注意要按照格式输出，逗号后⾯不带空格，不能直接输出ans
print(f"[{ans[0]},{ans[1]}]")