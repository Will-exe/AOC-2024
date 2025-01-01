
with open('pinput.txt', 'r') as file:
    txt = file.read()
    aList = txt.strip()
    aList = aList.split('\n')

print(aList)
W = 7
H = 7

grid: list[list[str]] = [['.' for i in range(W)] for j in range(H)]

i = 12

for pairs in aList:
    i -= 1
    if i >= 0:
        c, r = pairs.split(',')
        grid[int(r)][int(c)] = '#'

for line in grid:
    print(line)