t = int(input())
cases = list()
result = list()
for _ in range(t):
    temp = list()
    temp.append(int(input()))
    temp.append(list(map(int, input().split())))
    cases.append(temp)
for case in cases:
    n, data = case
    count = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                count += 1
    result.append(count)
for i in result:
    print(f"Optimal train swapping takes {i} swaps.")
