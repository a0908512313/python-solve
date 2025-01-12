m = int(input())
datas = list()
results = list()

for _ in range(m):
    datas.append(list(map(int, input().split())))

for data in datas:
    a, b, c = data
    temp = b**2 - 4*a*c
    if temp < 0:
        results.append("No")
    else:
        TEMP = 0
        while TEMP**2 < temp:
            TEMP += 1
        if TEMP**2 == temp:
            results.append("Yes")
        else:
            results.append("No")

for i in results:
    print(i)
