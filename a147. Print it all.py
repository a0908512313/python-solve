result = list()
while True:
    n = int(input())
    if n == 0:
        break
    else:
        temp = list()
        for i in range(1, n):
            if i % 7 != 0:
                temp.append(i)
        result.append(temp)
for i in result:
    print(" ".join(map(str, i)))
