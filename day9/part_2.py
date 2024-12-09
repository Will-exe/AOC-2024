
with open('input.txt', 'r') as file:
    txt = file.read()
    aList = txt.strip()

id = 0
vals = []
empty = []
for num in range(len(aList)):
    if int(num) % 2 == 0:
        val = [id, int(aList[num])]
        vals.append(val)
        id += 1
    else:
        empty.append(int(aList[num]))

if (k:= len(vals) - len(empty) > 0):
    empty.extend([0]*k) 
    
result = []
emptyBlocks = []
valBlocks = []
index = 0
for i, amt in vals:
    result.extend([i] * amt)
    result.extend(['.'] * empty[i])
    valBlocks.append([index, i, amt])
    index += amt
    emptyBlocks.append([index, empty[i]])
    index += empty[i]

"""
print()
print(result)
print()
print(valBlocks)
print(emptyBlocks)
print()
"""

isDone = False
#index, value, amount
for j in range(len(valBlocks)-1,-1,-1):
    index = valBlocks[j][0]
    value = valBlocks[j][1]
    amount = valBlocks[j][2]
    if isDone: break
    for i in range(len(emptyBlocks)):
        #if index < max(emptyBlocks[0]):
        #    isDone = True
        #    break
        if amount <= emptyBlocks[i][1] and index > emptyBlocks[i][0] :
            result[emptyBlocks[i][0]:emptyBlocks[i][0]+amount] = [value] * amount
            result[index:index+amount] = ['.'] * amount
            emptyBlocks[i][0] += amount
            emptyBlocks[i][1] -= amount
            break
        else:
            continue
print(result)

"""
i = 0
k = len(result) - 1
while i < k:
    if result[i] != '.':
        i += 1
        continue
    if result[k] == '.':
        k -= 1
        continue
    result[i] = result[k]
    i += 1
    k -= 1

result = result[:i+1]
#print(result)
"""


checksum = 0
for i in range(len(result)):
    if result[i] != '.':
        checksum += i * result[i]

print(checksum)

