n, w = map(int, input().split())
req = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    req.append(temp[1:])
day = -1
total = 0
for i in range(n):
    total += w
    total -= sum(req[i])
    if total < 0:
        day = i+1
        break
print(day)
