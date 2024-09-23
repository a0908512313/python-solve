n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

value = [max(i) for i in num]

MAX = sum(value)

can = [i for i in value if MAX % i == 0]

print(MAX)

if len(can) == 0:
    print('-1')
else:
    print(' '.join(map(str, can)))
