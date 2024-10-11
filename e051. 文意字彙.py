n = input()
result = str()
for i in range(len(n)):
    if i == 0 or i == len(n) - 1:
        result+=n[i]
    else:
        result+='_'
print(result)
