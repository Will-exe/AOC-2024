import copy

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
isLoop = False
numLoops = 0
bList = copy.deepcopy(aList)

for x in range(len(aList)):
    for z in range(len(aList[x])):

        aList = copy.deepcopy(bList)
        aList[x][z] = '#'
        isLoop = False
        done = False

        for rIndex, cIndex, char in loc:
            aList[rIndex][cIndex] = 'X'
            count += 1
            k = dKeys.index(char)
            while done == False:
                key = dKeys[k % len(dKeys)]
                dr, dc = directions[key]

                if key == ">" or key == "<":
                    line = '-'
                else:
                    line = '|'
                
                i = 1
                while (0 <= rIndex - dr * i <= rLen - 1 and 0 <= cIndex - dc*i <= cLen - 1):
                    if aList[rIndex - dr*i][cIndex - dc*i] != '#':
                        if aList[rIndex - dr*i][cIndex - dc*i] != 'X':
                            aList[rIndex - dr*i][cIndex - dc*i] = 'X'
                            contLines = 0
                            count += 1
                        i += 1
                    else:
                        break
                    contLines += 1

                    if contLines > 10000:
                        isLoop = True
                        break

                k += 1
                if not (0 <= rIndex - dr * i <= rLen - 1 and 0 <= cIndex - dc*i <= cLen - 1):
                    done = True
                    break

                if isLoop:
                    break

                i -= 1
                rIndex = rIndex - dr*i
                cIndex = cIndex - dc*i
        if isLoop:
            numLoops += 1
        print(numLoops)
        #for line in aList:
        #    for char in line:
        #        print(char, end='')
        #    print()
        #print()

            
print(numLoops)

#for line in aList:
#    for char in line:
#        print(char, end='')
#    print()