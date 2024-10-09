h, w, n = map(int, input().split())
plate = [[0 for _ in range(w)] for _ in range(h)]
actions = list()
for _ in range(n):
    actions.append(list(map(int, input().split())))

for action in actions:
    r, c, t, x = action
    for i in range(h):
        for j in range(w):
            if abs(i - r) + abs(j-c) <= t:
                plate[i][j] += x

for i in plate:
    print(" ".join(map(str, i)))
