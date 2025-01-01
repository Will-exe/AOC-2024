from functools import *

with open('pinput.txt', 'r') as file:
    grid = file.read().strip().split('\n')

rLen = len(grid)
cLen = len(grid[0])
visited = [[False] * cLen for row in range(rLen)]
regions = []

@cache
def checkAdjacentFences(letter, row, col):
    dirs = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1),
    }

    numAdjacents = 0
    for dir, (r, c) in dirs.items():
        if 0 <= r < rLen and 0 <= c < cLen:
            #print("row: ", r)
            #print("col: ", c)
            #print("grid row: ", grid[r])
            #print("char: ", grid[r][c])
            numAdjacents += (letter != grid[r][c])
        else: 
            numAdjacents += 1
    return numAdjacents

def findOutsideCorners(region):
    corners = 0
    for char, r, c in region:
        if (numAdj := checkAdjacentFences(char, r, c)) == 2:
            corners += 1
        elif numAdj == 3:
            corners += 2
        elif numAdj == 4:
            corners += 4
    return corners

def findInsideCorners(region):
    #Find blocks of 4
    #Make blocks in dirs
    #Save blocks into list of visited blocks
    visited = []
    
    corners = 0
    for char, r, c in region:
        dirs = {
        "upleft": ((r - 1, c -1), (r - 1, c), (r, c - 1), (r, c)),
        "upright": ((r - 1, c + 1), (r - 1, c), (r, c + 1), (r, c)),
        "downleft": ((r + 1, c - 1), (r + 1, c), (r, c - 1), (r, c)),
        "downright": ((r + 1, c + 1), (r + 1, c), (r, c + 1), (r, c)),
        }
        for dir, (r2, c2) in dirs.items():
            if any((row == r2 and col == c2) for _, row, col in region):
                if checkAdjacentFences(char, r, c) > 0 and checkAdjacentFences(char, r2, c2) > 0:
                    nDirs = {
                        "up": (r2 - 1, c2),
                        "down": (r2 + 1, c2),
                        "left": (r2, c2 - 1),
                        "right": (r2, c2 + 1),
                    }
                    if dir == "upleft":
                        notUp = any
                    elif dir == "upright":
                    elif dir == "downleft":
                    elif dir == "downright":
                    corners += 1
                    index = region.index((char, r2, c2))
                    visited[index] == True

    return corners

def countSides(region):
    sides = 0

    miR = min(region, key=lambda x: x[1])
    maR = max(region, key=lambda x: x[1])
    miC = min(region, key=lambda x: x[2])
    maC = max(region, key=lambda x: x[2])

    print(miR, maR)
    
    #left + right
    prevMaxCol = -1
    prevMinCol = -1
    for i in range(miR[1], maR[1]+1):
        cols = [c for char, r, c in region if r == i]
        maxC = max(cols)
        minC = min(cols)
        if maxC != prevMaxCol:
            #print("max col ", maxC, "previous max col", prevMaxCol)
            sides += 1
        if minC != prevMinCol:
            #print("min col ", minC,"previous min col ", prevMinCol)
            sides += 1
        prevMaxCol = maxC
        prevMinCol = minC

    #CFVI
    #top + down
    prevMaxRow = -1
    prevMinRow = -1
    for i in range(miC[2], maC[2]+1):
        rows = [r for char, r, c in region if c == i]
        maxR = max(rows)
        minR = min(rows)
        if maxR != prevMaxRow:
            #print("max row ", maxR, "previous max row", prevMaxRow)
            sides += 1
        if minR != prevMinRow:
            print("min row ", minR, "previous min row", prevMinRow)
            sides += 1
        prevMaxRow = maxR
        prevMinRow = minR
    
    return sides


def dfs(r, c, char, cRegion):
    if 0 <= r < rLen and 0 <= c < cLen and grid[r][c] == char and not visited[r][c]:
        visited[r][c] = True
        cRegion.append((char, r, c))

        dfs(r+1,c,char,cRegion)
        dfs(r-1,c,char,cRegion)
        dfs(r,c+1,char,cRegion)
        dfs(r,c-1,char,cRegion)
    else:
        return

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if not visited[row][col]:
            cRegion = []
            dfs(row,col,grid[row][col], cRegion)
            regions.append(cRegion)

results = []
for region in regions:
    cResults = [region[0][0],0,0]
    for x in region:
        cResults[1] += 1
    iCorners = findInsideCorners(region)
    oCorners = findOutsideCorners(region)
    print(region[0][0], " sides: ", iCorners + oCorners)
    cResults[2] = iCorners + oCorners
    results.append(cResults)

numFences = 0
for char, area, sides in results:
    price = area * sides
    print("Region ", char, " price: ", area, "*", sides, "=", price)
    numFences += price
print(numFences)
    