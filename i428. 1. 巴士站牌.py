n = int(input())
data = list()
for _ in range(n):
    data.append(list(map(int, input().split())))


dis = []
for i in range(1, n):
    x1, y1 = data[i-1]
    x2, y2 = data[i]
    dis.append(abs(x2 - x1) + abs(y2 - y1))

print(max(dis), min(dis))
