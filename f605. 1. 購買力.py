n, d = map(int, input().split())
price = []
num = 0
total = 0

for i in range(n):
    price.append(list(map(int, input().split())))

for i in range(n):
    if (max(price[i]) - min(price[i])) >= d:
        num += 1
        total += sum(price[i]) // 3

print(f'{num} {total}')
