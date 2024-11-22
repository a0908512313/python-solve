TEMP = list(map(int, input().split()))
n, m = TEMP
data = list()
for _ in range(n):
    data.append(list(map(int, input().split())))

result = list()
for i in range(n):
    for j in range(m):
        x = data[i][j]
        temp = 0
        for a in range(n):
            for b in range(m):
                if abs(a-i) + abs(b-j) <= x:
                    temp += data[a][b]
        if temp % 10 == x:
            result.append((i, j))
print(len(result))
for i in result:
    j = list(i)
    print(j[0], j[1])
