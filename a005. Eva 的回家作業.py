n = int(input())
data = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

for i in data:
    if i[-1] - i[-2] == i[-2] - i[-3]:
        i.append(i[-1] + (i[-1] - i[-2]))
    else:
        i.append(i[-1] * (i[-1] // i[-2]))
    print(' '.join(map(str, i)))
