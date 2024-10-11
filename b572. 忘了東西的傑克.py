n = int(input())
result = list()
data = list()
for _ in range(n):
    data.append(list(map(int, input().split())))

for data in data:
    h1, m1, h2, m2, m3 = data
    first = h1*60 + m1
    second = h2*60 + m2
    if second >= first+m3:
        result.append("Yes")
    else:
        result.append("No")
for i in result:
    print(i)
