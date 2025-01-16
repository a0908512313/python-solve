while True:
    try:
        n, m = map(int, input().split())
        count, total = 0, 0

        while True:
            total += n
            n += 1
            count += 1
            if total > m:
                break
        print(count)
    except EOFError:
        break
