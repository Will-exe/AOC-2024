from math import gcd
import numpy as np

with open('input.txt', 'r') as file:
    txt = file.read()
    grid = txt.strip().split('\n') 

def findWholeSlope(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2

    if x1 == x2:
        return None
    else:
        dX = x2 - x1
        dY = y2 - y1
        gcD = gcd(dX, dY)
        return dX//gcD, dY//gcD


def findPairs(lines):
    charLoc = {}
    for rId, row in enumerate(lines):
        for cId, char in enumerate(row):
            if char != '.':
                if char not in charLoc:
                    charLoc[char] = []
                charLoc[char].append((rId,cId))
    
    pairs = {}
    for char, loc in charLoc.items():
        pairs[char] = []
        for i in range(len(loc)):
            for j in range(i+1, len(loc)):
                slope = findWholeSlope(loc[i], loc[j])
                pairs[char].append((np.array(loc[i]),np.array(loc[j]), np.array(slope)))
    
    return pairs

pairs = findPairs(grid)
antiNodeCount = 0
antiNodeLoc = []

for char, vals in pairs.items():
    for loc1, loc2, slope in vals:
        i = 0
        inBound = True
        overflow1 = False
        overflow2 = False
        while overflow1 == False or overflow2 == False:
            if overflow1 == False:
                antiLoc = loc1 - slope * i
                if 0 <= antiLoc[0] < len(grid[0]) and 0 <= antiLoc[1] < len(grid):
                    antiNodeLoc.append(antiLoc)
                else: 
                    overflow1 = True
            if overflow2 == False:
                antiLoc = loc2 + slope * i
                if 0 <= antiLoc[0] < len(grid[0]) and 0 <= antiLoc[1] < len(grid):
                    antiNodeLoc.append(antiLoc)
                else:
                    overflow2 = True
            i += 1

        #print(loc1, loc2, slope)
        #print(loc1 - slope)
        #print(loc2 + slope)

antiNodeLoc = np.array(antiNodeLoc)
print(antiNodeLoc)
antiNodeLoc = np.unique(antiNodeLoc, axis = 0)
print(antiNodeLoc)

antiNodeCount = len(antiNodeLoc)
print(antiNodeCount)

aList = [[char for char in line.strip()] for line in grid]
for node in antiNodeLoc:
    aList[node[0]][node[1]] = '#'

for line in aList:
    for char in line:
        print(char, end='')
    print()