from functools import *
with open('input.txt', 'r') as file:
    txt = file.read().strip().split(' ')

#test = ['125', '17']
#txt = test
txt = [int(item) for item in txt]


@cache
def get_divs(num, rBlink):
    if rBlink == 0:
        return 1
    if num == 0:
        return get_divs(1, rBlink - 1)
    if len(str(num)) > 1 and len(str(num)) % 2 == 0:
        k = len(str(num)) // 2
        right = get_divs(int(str(num)[k:]), rBlink - 1)
        left = get_divs(int(str(num)[:k]), rBlink - 1)
        return right + left
    else:
        return get_divs(num * 2024, rBlink - 1)


result = 0
k = 75
for stone in txt:
    result += get_divs(stone, k)
print(result)