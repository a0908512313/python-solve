n = int(input())
result = []
for i in range(9, 1, -1):
    while n % i == 0:
        n //= i
        result.append(i)
if n > 1 or not result:
    print("-1")
else:
    result.sort()
    print(" ".join(map(str, result)))
