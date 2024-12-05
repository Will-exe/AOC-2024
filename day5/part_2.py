
with open('input.txt', 'r') as file:
    rules = []
    lists = []
    lines = file.readlines()
    i = 0
    while len(lines[i]) > 1:
        rules.append(lines[i].strip().split('|'))
        i += 1
    i += 1
    while i < len(lines):
        lists.append(lines[i].strip().split(','))
        i += 1

        """
    for line in lines[:1176]:
        rules.append(line.strip().split('|'))
    for line in lines[1177:]:
        lists.append(line.strip().split(','))
        """

rDict = {}

for key, val in rules:
    if key not in rDict:
        rDict[key] = []
    rDict[key].append(val)

#rDict['13'] = []


result = []
for x in lists:
    overlap = []
    j = x[:]
    for i in x:
        overlap.append(len(set(rDict[i]) & set(x)))
    newList = []
    for i in range(len(x)):
        index = overlap.index(max(overlap))
        newList.append(x[index])
        del overlap[index]
        del x[index]
    if j != newList:
        result.append(newList)

midNums = [int(x[len(x)//2]) for x in result]
for x in result:
    print(x)

print(midNums)
print(sum(midNums))