n = int(input())
data = (list(map(int, input().split())))
result = list()


for i in range(1, n+1):
    first = data.index(i)
    second = data[first+1:].index(i)+first+1
    count = 0
    for a in range(first+1, second):
        if data[a] < i:
            count += 1
    result.append(count)
print(sum(result))
