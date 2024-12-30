data = list(input())
target = input()
result = [-1] * len(target)
for i in range(len(target)):
    for j in range(len(data)):
        if target[i] == data[j]:
            result[i] = j+1
            data[j] = ' '
            break

output = ""
for i in result:
    if i == -1:
        output += 'X '
    else:
        output += str(i) + " "

print(output.strip())
