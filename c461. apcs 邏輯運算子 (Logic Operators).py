a, b, c = map(int, input().split())

found = False

if (a and b) == c:
    print("AND")
    found = True

if (a or b) == c:
    print("OR")
    found = True

if (a ^ b) == c:
    print("XOR")
    found = True

if not found:
    print("IMPOSSIBLE")
