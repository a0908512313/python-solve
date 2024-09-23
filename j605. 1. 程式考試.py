n = int(input())
data = list()

for _ in range(n):
    data.append(list(map(int, input().split())))


score = list()
error = 0
for i in range(n):
    score.append(data[i][1])
    if data[i][1] == -1:
        error += 1
total = max(score) - n - error * 2

if total < 0:
    total = 0

index = data[score.index(max(score))][0]

print(total, index)
