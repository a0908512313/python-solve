n = int(input())
data = list()
for _ in range(2*n):
    data.append(list(map(int, input().split())))

result = ""
for i in range(n):
    first = data[i*2]
    second = data[i*2+1]

    wrong = ""

    if first[1] == first[3] or first[1] != first[5] or second[1] == second[3] or second[1] != second[5]:
        wrong += "A"

    if first[6] != 1 or second[6] != 0:
        wrong += "B"

    if first[1] == second[1] or first[3] == second[3] or first[5] == second[5]:
        wrong += "C"

    if wrong != "":
        result += wrong + "\n"

if result == "":
    result = "None"

print(result)
