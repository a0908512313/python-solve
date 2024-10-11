n = int(input())
actions = list()
for _ in range(n):
    actions.append(list(map(int, input().split())))
result = list()
for action in actions:
    k = action[0]
    if k == 1:
        result.append(action[1])
    elif k == 2:
        if len(result)!=0:
            print(result[0])
        else:
            print("-1")
    elif k == 3:
        if len(result)!=0:
            result.pop(0)
        else:
            continue
