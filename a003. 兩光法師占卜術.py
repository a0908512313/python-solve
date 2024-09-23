M, D = map(int, input().split())
r = (M*2+D) % 3

if r == 0:
    print("普通")
elif r == 1:
    print("吉")
elif r == 2:
    print("大吉")
