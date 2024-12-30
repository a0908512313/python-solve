firstList = list(map(int, input().split()))
secondList = list(map(int, input().split()))
current = firstList
output = list()


def process(list):
    if list[0] % 3 == 0:
        MAX = max(list)
        for i in range(len(list)):
            if list[i] == MAX:
                list[i] //= 2
        return MAX
    else:
        MIN = min(i for i in list if i != 0)
        for i in range(len(list)):
            if list[i] == MIN:
                list[i] -= 1
        return MIN


while True:
    result = process(current)
    output.append(result)
    if result % 2 == 0:
        current = secondList
    else:
        current = firstList
    if result == 0:
        break

for i in output:
    print(str(i), end='\n')
