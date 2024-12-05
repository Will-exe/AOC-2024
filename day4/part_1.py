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

targetWord = "XMAS"

rowLen = len(aList)
colLen = len(aList[0])
wLen = len(targetWord)

directions = {
        "Right": (0, 1),
        "Left": (0, -1),
        "Bottom": (1, 0),
        "Top": (-1, 0),
        "Top Right": (-1, 1),
        "Top Left": (-1, -1),
        "Bottom Left": (1, -1),
        "Bottom Right": (1, 1)
    }

pos = []

for num, line in enumerate(aList):
    matches = re.finditer(r'X', line)
    for match in matches:
        pos.append((num, match.start()))

isMatch = True
matchCount = 0

for r, c in pos:
    for direction, (dr, dc) in directions.items():
        #BOUND CHECKING
        if direction == "Right" and c + (wLen - 1) > rowLen:
            continue
        elif direction == "Left" and c - (wLen - 1) < 0:
            continue
        elif direction == "Bottom" and r + (wLen - 1) > colLen:
            continue
        elif direction == "Top" and r - (wLen - 1) < 0:
            continue
        elif direction == "Top Right" and (r - (wLen - 1) < 0 or c + (wLen - 1) > rowLen):
            continue
        elif direction == "Top Left" and  (r - (wLen - 1) < 0 or c - (wLen - 1) < 0):
            continue
        elif direction == "Bottom Left" and (r + (wLen - 1) > colLen or  c - (wLen - 1) < 0):
            continue
        elif direction == "Bottom Right" and (r + (wLen - 1) > colLen or c + (wLen - 1) > rowLen):
            continue
             
        isMatch = True
        
        for i in range(4):
                try:
                    if aList[r + dr * i][c + dc * i] != targetWord[i]:
                        isMatch = False
                        break
                except IndexError as e:
                     isMatch = False
                     break

        if isMatch == True:
            matchCount += 1

print(matchCount)
