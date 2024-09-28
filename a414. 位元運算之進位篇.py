import sys
for data in sys.stdin:
    data = data.strip() 
    if data == "0":
        break
    n = bin(int(data) + 1)[2:][::-1]
    n = [i for i in n]
    print(n.index("1"))
