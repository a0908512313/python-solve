n = input()
result = list()
data = [chr(i) for i in range(65, 91)]
for i in range(6):
    result.append(abs(data.index(n[i]) - data.index(n[i+1])))
print("".join(map(str, result)))
