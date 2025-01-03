n = int(input())
price = list(map(int, input().split()))
buy = list()
while True:
    temp = list(map(int, input().split()))
    if temp == [0, 0]:
        break
    else:
        buy.append(temp)
total = 0
for i in buy:
    x, g = i
    total += price[x-1]*g
print(total)
