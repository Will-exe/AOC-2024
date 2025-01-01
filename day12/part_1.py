from functools import *

with open('input.txt', 'r') as file:
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
    for char, row, col in region:
        cResults[1] += checkAdjacentFences(char, row, col)
        cResults[2] += 1
    results.append(cResults)

numFences = 0
for char, area, perimeter in results:
    price = area * perimeter
    print("Region ", char, " price: ", area, "*", perimeter, "=", price)
    numFences += price
print(numFences)
    