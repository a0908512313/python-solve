n = int(input())

data = list()
for _ in range(n):
    data.append(list(map(int, input().split())))


result = str()

for i in range(n):
    if data[i][0] > data[i][1]:
        result += ">\n"
    if data[i][0] < data[i][1]:
        result += "<\n"
    if data[i][0] == data[i][1]:
        result += "=\n"

print(result)
