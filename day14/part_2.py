import re
import math

data = []

#Read data, keeping only the numbers
with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        nums = re.findall(r"-?\d+", line)
        #print(nums)
        nums = list(map(int,nums))
        data.append(nums)


def updateGrid(i):
    for val in data:
        x = int(math.fmod(val[0] + val[2]*i, len(grid[0])))
        y = int(math.fmod(val[1] + val[3]*i, len(grid)))
        #print("x: ", x)
        #print("y: ", y)
        if grid[y][x] == '.':
            grid[y][x] = 1
        else:
            grid[y][x] += 1

bla = False
i = 1
while bla != True:
    grid = [['.' for _ in range(101)] for _ in range(103)]
    updateGrid(i)

    for line in grid:
        for char in line:
            print(char, end='')
    print()
    print(i)
    i += 1
    input("Please press any key...")


"""
P1 stuff

#Find robot locations
for val in data:
    x = int(math.fmod(val[0] + val[2]*100, len(grid[0])))
    y = int(math.fmod(val[1] + val[3]*100, len(grid)))
    #print("x: ", x)
    #print("y: ", y)
    if grid[y][x] == '.':
        grid[y][x] = 1
    else:
        grid[y][x] += 1

#Section off quadrants

if len(grid) % 2 == 1:
    rMid = math.floor(len(grid) / 2)
    grid = [row for i, row in enumerate(grid) if i != rMid]

if len(grid[0]) % 2 == 1:
    cMid = math.floor(len(grid[0]) / 2)
    grid = [row[:cMid] + row[cMid+1:] for row in grid]

rMid = int(len(grid) / 2) 
cMid = int(len(grid[0]) / 2)

#print(rMid, cMid)
#print(len(grid), len(grid[0]))

tLeft = [row[:cMid] for row in grid[:rMid]]
tRight = [row[cMid:] for row in grid[:rMid]]
bLeft = [row[:cMid] for row in grid[rMid:]]
bRight = [row[cMid:] for row in grid[rMid:]]

tLSum = sum(int(value) for row in tLeft for value in row if isinstance(value, int)) 
tRSum = sum(int(value) for row in tRight for value in row if isinstance(value, int))
bLSum = sum(int(value) for row in bLeft for value in row if isinstance(value, int))
bRSum = sum(int(value) for row in bRight for value in row if isinstance(value, int)) 

safetyFactor = tLSum * tRSum * bLSum * bRSum
"""


"""
Debug

for line in grid:
    for char in line:
        print(char, end='')
    print()
print()
print()
print("bLeft")
for line in bLeft:
    for char in line:
        print(char, end='')
    print()
"""
    
#print(tLSum,tRSum,bLSum,bRSum)
#print("Safety factor: ", safetyFactor)