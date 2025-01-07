def func(n):
    temp = [i for i in range(1, n) if n % i == 0]
    SUM = sum(temp)
    if SUM == n:
        return "PERFECT"
    elif SUM < n:
        return "DEFICIENT"
    else:
        return "ABUNDANT"


result = ["PERFECTION OUTPUT"]
datas = list(map(int, input().split()))
for data in datas:
    result.append(f'{data:5}  {func(data)}')
result.append("END OF OUTPUT")
for i in result:
    print(i)
