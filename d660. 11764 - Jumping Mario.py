t = int(input())
result = list()

for a in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    high = 0
    low = 0
    for i in range(n - 1):
        if data[i+1] > data[i]:
            high += 1
        elif data[i+1] < data[i]:
            low += 1
    result.append(f'Case {a+1}: {high} {low}')

for i in range(t):
    print(result[i])
