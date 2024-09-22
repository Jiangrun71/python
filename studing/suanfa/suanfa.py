#split(",") 拆分输入字符串为⼀个列表 input().split(",")
riddles = input().split(",")
answers = input().split(",")
# 初始化结果列表res = []
res = list()

 # 构建谜底库answers_dic，其中
 # key为每⼀个谜底answer去重后排序的结果a
 # value为每⼀个谜底answer⾃⾝
# 初始化answers_dic = {}
answers_dic = dict()

# 遍历每⼀个谜底answer 
for answer in answers:
    a = "".join(sorted(set(answer))) #  
    answers_dic[a] = answer


# 遍历每⼀个谜⾯riddle
for riddle in riddles:
# 得到riddle去重后排序的结果r
    r = "".join(sorted(set(riddle)))
# 查看r是否位于谜底库中
# 若在则将对应的谜底answers_dic[r]加⼊res中
# 否则储存字符串"not found"
    if r in answers_dic:
        res.append(answers_dic[r])
    else:
        res.append("not found")


print(",".join(res))