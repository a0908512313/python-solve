a, b, c = map(int, input().split())

f = b**2 - (4 * a * c)
if f < 0:
    print("No real root")
elif f == 0:
    print(f'Two same roots x={int((-b + f**0.5) // (2*a))}')
else:
    first = (-b + f**0.5) // (2*a)
    second = (-b - f**0.5) // (2*a)
    print(f'Two different roots x1={
          int(max(first, second))} , x2={int(min(first, second))}')
