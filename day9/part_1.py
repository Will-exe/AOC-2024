
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

for i, val in vals:
    #print(i, val, empty[i])
    result.extend([i] * val)
    result.extend(['.'] * empty[i])

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
    result[k] = '.'
    i += 1
    k -= 1

#print(result)
result = result[:i+1]
#print(result)

checksum = 0
for i in range(len(result)):
    checksum += i * result[i]

print(checksum)
