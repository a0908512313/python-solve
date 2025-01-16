while True:
    try:
        s = input()
        s = ''.join(c.lower() for c in s if c.isalpha())

        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        odd_count = sum(1 for v in count.values() if v % 2 == 1)
        print("yes !" if odd_count <= 1 else "no...")

    except EOFError:
        break
