n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
for data in datas:
    data = data[1:]
    print(f'{round(sum(data)/len(data), 2):.2f}')
