import sys

data = sys.stdin.read().split()
for n in data:
    print(bin(int(n))[2:])
