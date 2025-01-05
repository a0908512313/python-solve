n = list(input())
k = int(input())
actions = list(int(input()) for _ in range(k))
for action in actions:
    if action == 0:
        temp = list()
        for i in range(0, len(n), 2):
            temp.append([n[i+1], n[i]])
        n = list()
        for i in temp:
            n.extend(i)
    elif action == 1:
        temp = list()
        for i in range(0, len(n), 2):
            a, b = n[i], n[i+1]
            temp.append(sorted([a, b]))
        n = list()
        for i in temp:
            n.extend(i)

    else:
        a, b, temp = list(), list(), list()
        for i in range(len(n)):
            if i < len(n)//2:
                a.append(n[i])
            else:
                b.append(n[i])
        for i in range(len(n)//2):
            temp.append([a[i], b[i]])
        n = list()
        for i in temp:
            n.extend(i)
print(''.join(n))
