while True:
    try:
        v, t = map(int, input().split())
        x = 2 * v * t
        print(x)
    except EOFError:
        break
