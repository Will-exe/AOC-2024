DIRS = [(0,1), (1, 0), (-1, 0), (0, -1)]

def explore_grid(current: tuple[int, int], target: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    if target == 10:
        return [current]
    result: list[tuple[int, int]] = []
    h = len(grid)
    w = len(grid[0])
    for dir in DIRS:
        if 0 <=current[0] + dir[0] < h and 0 <= current[1] + dir[1] < w:
            if grid[current[0]+dir[0]][current[1]+dir[1]] == target:
                result.extend(explore_grid((current[0]+dir[0],current[1]+dir[1]), target + 1, grid))
    return result


with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = [[int(i) for i in line.strip()] for line in lines]

result = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == 0:
            result += len(explore_grid((y, x), 1, grid))

print(result)



"""


with open('pinput.txt', 'r') as file:
    txt = file.read()
    aList = txt.strip().split('\n')

aList = [[int(num) for num in line] for line in aList]

directions = {
        "Right": (0, 1),
        "Left": (0, -1),
        "Bottom": (1, 0),
        "Top": (-1, 0)
}

h = len(aList)
w = len(aList[0])
result = []
count = 0

def findNextSpot(index, num):
    inResult = []
    if num == 10:
        return [index]
    for direction, (dr, dc) in directions.items():
        if 0 <= index[0] + dr <= h - 1 and 0 <= index[1] + dc <= w - 1:
            if aList[index[0]+dr][index[1]+dc] == num:
                inResult.extend(findNextSpot([index[0]+dr,index[1]+dc], num+1))
    return inResult
            

for i in range(len(aList)):
    for j in range(len(aList[0])):
        if aList[i][j] == 0:
            result.append(findNextSpot([i,j], 1))

for trailhead in result:
    print(trailhead)


"""