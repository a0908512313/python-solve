B = int(input())
P = int(input())
stops = [0] * B

for _ in range(P):
    a, b = sorted(map(int, input().split()))
    for i in range(a - 1, b):
        stops[i] += 1

min_stop = min(stops)
max_stop = max(stops)
minIndex = stops.index(min_stop) + 1
maxIndex = len(stops) - 1 - stops[::-1].index(max_stop) + 1

print(minIndex, maxIndex)
