n, d = map(int, input().split())
data = list(map(int, input().split()))

have = 0
result = 0
lastIN = 0
lastOUT = 0

for i in range(n):
    if have == 0:
        if i == 0 or data[i] <= lastOUT - d:
            have = 1
            lastIN = data[i]
    else:
        if data[i] >= lastIN + d:
            have = 0
            result += data[i] - lastIN
            lastOUT = data[i]

print(result)
