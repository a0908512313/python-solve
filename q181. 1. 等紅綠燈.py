a, b = map(int, input().split())
n = int(input())
data = list(map(int, input().split()))
T = a+b
result = 0
for i in data:
    temp = i % T
    if temp > a:
        result += b - (temp - a)
    elif temp == a:
        result += b
print(result)
