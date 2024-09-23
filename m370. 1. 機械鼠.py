x, n = map(int, input().split())
data = list(map(int, input().split()))

big = [i for i in data if i > x]
small = [i for i in data if i < x]

num = max(len(big), len(small))
pos = max(big) if num == len(big) else min(small)


print(num, pos)
