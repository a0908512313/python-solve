n = int(input())
data = list(map(int, input().split()))

result = 0

for i in range(n):
    if data[i] == 0:
        if i == 0:
            result += data[i+1]
        elif i == n - 1:
            result += data[i-1]
        else:
            result += min(data[i-1], data[i+1])

print(result)
