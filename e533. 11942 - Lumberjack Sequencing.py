n = int(input())
data = list()
for _ in range(n):
    data.append(list(map(int, input().split())))

result = "Lumberjacks:"
for i in range(n):
    if data[i] == sorted(data[i]) or data[i] == sorted(data[i], reverse=True):
        result += "\nOrdered"
    else:
        result += "\nUnordered"

print(result)
