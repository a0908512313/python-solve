n = int(input())
actions = list()
for _ in range(n):
    actions.append(list(map(int, input().split())))
result = [0, 0]
for action in actions:
    a, b = action
    if a== 0:
        result[1]+=b
    elif a==1:
        result[0]+=b
    elif a==2:
        result[1]-=b
    elif a==3:
        result[0]-=b
print(result[0], result[1])
