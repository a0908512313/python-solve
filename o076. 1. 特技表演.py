n = int(input())
data = list(map(int, input().split()))

temp = 1
results = []
for j in range(n-1):
    if data[j] > data[j+1]:
        temp += 1
    else:
        results.append(temp)
        temp = 1
results.append(temp)
print(max(results))
