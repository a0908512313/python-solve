a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_cost = float('inf')
best_a, best_b = -1, -1

for i in range(10):
    for j in range(i, 10):
        days = j - i
        total_cost = a[i] + b[j] + days * 1000
        if total_cost < min_cost:
            min_cost = total_cost
            best_a, best_b = i + 1, j + 1

print(best_a, best_b, min_cost)
