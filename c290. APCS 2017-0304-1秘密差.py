n = input()
first, second = 0, 0

for i in range(len(n)):
    if i % 2 == 0:
        first += int(n[i])
    else:
        second += int(n[i])

print(abs(first - second))
