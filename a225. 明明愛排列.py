while True:
    try:
        n = int(input())
        data = list(map(int, input().split()))
        data.sort(key=lambda x: (x % 10, -x))
        print(' '.join(map(str, data)))
    except EOFError:
        break
