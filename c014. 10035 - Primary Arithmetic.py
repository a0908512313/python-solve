while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    carry_count = 0
    carry = 0

    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
        a //= 10
        b //= 10

    if carry_count == 0:
        print("No carry operation.")
    elif carry_count == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")
