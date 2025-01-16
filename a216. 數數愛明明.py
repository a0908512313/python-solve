while True:
    try:
        n = int(input())
        if n == 1:
            print("1 1")
        else:
            f, g = 1, 1
            for i in range(2, n + 1):
                f += i
                g += f
            print(f"{f} {g}")
    except EOFError:
        break
