n = int(input())
datas = []
for _ in range(n):
    temp = []
    for _ in range(2):
        temp.append(list(map(int, input().split())))
    datas.append(temp)

result = []
for data in datas:
    x, y, z, w, n, m = data[0]
    actions = data[1]
    poison_count = 0
    dead = False

    for action in actions:
        m -= n * poison_count
        if m <= 0:
            result.append("bye~Rabbit")
            dead = True
            break
        if action == 1:
            m += x
        elif action == 2:
            m += y
        elif action == 3:
            m -= z
        elif action == 4:
            poison_count += 1
            m -= w

        if m <= 0:
            result.append("bye~Rabbit")
            dead = True
            break

    if not dead:
        result.append(f'{m}g')

for i in result:
    print(i)
