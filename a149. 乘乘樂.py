t = int(input())
result = list()
data = list()
for _ in range(t):
    data.append(input())
for i in data:
    temp = 1
    for j in range(len(i)):
        temp *= int(i[j])
    result.append(temp)
for i in result:
    print(i)
