f, s = map(int, input().split())
result = list()
for i in range(f, s+1):
    t = len(str(i))
    temp = 0
    for j in str(i):
        temp+=int(j)**t
    if temp == i:
        result.append(i)
if not result:
    print("none")
else:
    print(' '.join(map(str, result)))
