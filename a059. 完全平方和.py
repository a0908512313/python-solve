t = int(input())
cases = list()
result = list()
for _ in range(t):
    a = int(input())
    b = int(input())
    temp = list()

    def check(n):
        x = 0
        while x**2 < n:
            x += 1
        return x**2 == n
    for i in range(a, b+1):
        if check(i):
            temp.append(i)
    result.append(temp)

for i in range(len(result)):
    temp = sum(result[i])
    print(f'Case {i+1}: {temp}')
