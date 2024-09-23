n = int(input())

factors = {}
div = 2

while n > 1:
    count = 0
    while n % div == 0:
        n //= div
        count += 1
    if count > 0:
        factors[div] = count
    div += 1

result = []
for prime, power in factors.items():
    if power == 1:
        result.append(f"{prime}")
    else:
        result.append(f"{prime}^{power}")

print(" * ".join(result))
