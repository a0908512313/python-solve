n = list(input().split())
data = list(input().split())
data_dic = {}
for i in data:
    if i in n and i not in data_dic:
        data_dic[i] = 1
    else:
        data_dic[i] += 1
if len(data_dic.keys()) == len(n):
    print(min(data_dic.values()))
else:
    print("0")
