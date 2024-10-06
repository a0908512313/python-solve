n = int(input())
for _ in range(n):
    A, B, C = map(int, input().split())
    temp = [i for i in range(A + 1, B) if i % C != 0]
    if temp:
        print(" ".join(map(str, temp)))
    else:
        print("No free parking spaces.")
