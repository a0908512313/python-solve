n = int(input())
datas = list()
result = 0
for _ in range(n):
    datas.append(list(map(int, input().split())))
datas.sort(key=lambda x: -x[0])
current = 0
for fire, time in datas:
    current += time
    result += fire * current
print(result)
