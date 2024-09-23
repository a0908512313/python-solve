data = list()

while True:
    try:
        n = input()
        if n == '':
            break
        else:
            data.append(int(n))
    except EOFError:
        break

for i in data:
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print("閏年")
    else:
        print("平年")
