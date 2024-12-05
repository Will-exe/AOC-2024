import re

aList = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        aList.append(line)

pList = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

rowLen = len(aList)
colLen = len(aList[0])

pos = []

for num, line in enumerate(aList):
    matches = re.finditer(r'A', line)
    for match in matches:
        pos.append((num, match.start()))

matchCount = 0

for r, c in pos:
    #BOUND CHECKING
    if (r - 1 < 0 or c + 1 > rowLen or c - 1 < 0 or r + 1 > colLen ):
        continue

    try:
        if aList[r - 1][c + 1] == aList[r + 1][c + 1] == 'S' and aList[r + 1][c - 1] == aList[r - 1][c - 1] == 'M':
            print(r, c)
            matchCount += 1
            continue
        elif aList[r - 1][c + 1] == aList[r + 1][c + 1] == 'M' and aList[r + 1][c - 1] == aList[r - 1][c - 1] == 'S':
            print(r, c)
            matchCount += 1
            continue
        elif aList[r - 1][c + 1] == aList[r - 1][c - 1] == 'M' and aList[r + 1][c - 1] == aList[r + 1][c + 1] == 'S':
            print(r, c)
            matchCount += 1
            continue
        elif aList[r - 1][c + 1] == aList[r - 1][c - 1] == 'S' and aList[r + 1][c - 1] == aList[r + 1][c + 1] == 'M':
            print(r, c)
            matchCount += 1
            continue
    except IndexError as e:
            continue


print(matchCount)
