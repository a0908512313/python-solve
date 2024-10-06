n = int(input())
data = []
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
data.sort(key=lambda x: (x[0], x[1]))

now = list(map(int, input().split()))
now[1] += 20
if now[1] >= 60:
    now[1] -= 60
    now[0] += 1

temp_now = now[0] * 60 + now[1]
temp_data = [i[0] * 60 + i[1] for i in data]

result = None
for i, time in enumerate(temp_data):
    if temp_now <= time:
        result = data[i]
        break

if result is None:
    print("Too Late")
else:
    print('{:02d} {:02d}'.format(result[0], result[1]))
