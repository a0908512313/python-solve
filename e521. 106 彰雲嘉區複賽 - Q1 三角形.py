n = int(input())
results = []

for _ in range(n):
    sides = list(map(int, input().split()))
    sides.sort()
    a, b, c = sides

    if a + b <= c:
        results.append(0)
    else:
        if a == b or b==c or c==a:
            results.append([1, 1])
        else:
            results.append([1, 0])
for result in results:
    if isinstance(result, list):
        print(result[0], result[1])
    else:
        print(result)
