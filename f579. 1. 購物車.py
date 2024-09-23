a, b = map(int, input().split())
n = int(input())
cus = []
for _ in range(n):
    cus.append(list(map(int, input().split())))

total = 0

for i in range(n):
    A = 0
    B = 0
    for j in range(len(cus[i])):
        if abs(cus[i][j]) == a:
            if cus[i][j] > 0:
                A += 1
            else:
                A -= 1
        if abs(cus[i][j]) == b:
            if cus[i][j] > 0:
                B += 1
            else:
                B -= 1

    if A > 0 and B > 0:
        total += 1

print(total)
