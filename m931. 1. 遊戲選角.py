n = int(input())
data = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
data.sort(reverse=True, key=lambda x: (x[0] * x[0]) + (x[1] * x[1]))
print(data[1][0], data[1][1])
