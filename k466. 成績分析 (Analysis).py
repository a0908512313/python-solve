n, m = map(int, input().split())
datas = [list(map(int, input().split())) for _ in range(n)]

progress = []
regress = []

for data in datas:
    up_sum = 0
    down_sum = 0
    for i in range(m - 1):
        diff = data[i + 1] - data[i]
        if diff > 0:
            up_sum += diff
        elif diff < 0:
            down_sum += abs(diff)
    progress.append(up_sum)
    regress.append(down_sum)

best = min([i for i in range(n) if progress[i] == max(progress)])
worst = min([i for i in range(n) if regress[i] == max(regress)])

print(best + 1)
print(worst + 1)
