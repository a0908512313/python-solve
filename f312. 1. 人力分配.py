a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())
result = float('-inf')
for i in range(n+1):
    f = (a1 * i * i) + (b1 * i) + c1
    s = (a2 * (n-i) * (n-i)) + (b2 * (n-i)) + c2
    result = max(result, f+s)
print(int(result))
