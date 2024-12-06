import re

aList = []

with open('input.txt', 'r') as file:
    txt = file.read()
    aList = txt.strip().split('\n')
    #for line in lines:
    #    aList.append(line)

aList = [[char for char in line.strip()] for line in aList]
cLen = len(aList[0])
rLen = len(aList)


loc = []
guards = {'v', '>','<','^'}
for rIndex, string in enumerate(aList):
    for cIndex, char in enumerate(string):
        if char in guards:
            loc.append((rIndex, cIndex, char))

directions = {
        ">": (0, -1),
        "v": (-1, 0),
        "<": (0, 1),
        "^": (1, 0),
}

count = 0
dKeys = list(directions.keys())
done = False

for rIndex, cIndex, char in loc:
    aList[rIndex][cIndex] = 'X'
    count += 1
    k = dKeys.index(char)
    while done == False:
        dr, dc = directions[dKeys[k % len(dKeys)]]
        i = 1
        while (0 <= rIndex - dr * i <= rLen - 1 and 0 <= cIndex - dc*i <= cLen - 1):
            if aList[rIndex - dr*i][cIndex - dc*i] != '#':
                if aList[rIndex - dr*i][cIndex - dc*i] != 'X':
                    aList[rIndex - dr*i][cIndex - dc*i] = 'X'
                    count += 1
                i += 1
            else:
                break

        k += 1
        if not (0 <= rIndex - dr * i <= rLen - 1 and 0 <= cIndex - dc*i <= cLen - 1):
            done = True
            break

        i -= 1
        rIndex = rIndex - dr*i
        cIndex = cIndex - dc*i
    
print(count)

for line in aList:
    for char in line:
        print(char, end='')
    print()