
with open('input.txt', 'r') as file:
    rules = []
    lists = []
    lines = file.readlines()
    i = 0

    #Write the rule list
    while len(lines[i]) > 1:
        rules.append(lines[i].strip().split('|'))
        i += 1
    i += 1

    #Write the "update" list
    while i < len(lines):
        lists.append(lines[i].strip().split(','))
        i += 1

rDict = {}

#Store all rules per key
for key, val in rules:
    if key not in rDict:
        rDict[key] = []
    rDict[key].append(val)

result = []
for x in lists:
    overlap = []

    #Create an unaltered copy of "update" x
    j = x[:]

    #Create a list of length len(x), which stores the amount of overlap between the rules applied to a key, and each value in the list
    #
    # Intuition : If there is a single solution to each update, the value with the most overlap between its ruleset and the "update" line must be the first in the solution
    # Then, delete the value with the most overlap and go through each element in the list.
    #
    #
    for i in x:
        overlap.append(len(set(rDict[i]) & set(x)))
    outList = []

    #Find the index of the value with the most overlap, add that corresponding value to the output list, then remove them from both the overlap list and the input list (the "update")
    for i in range(len(x)):
        index = overlap.index(max(overlap))
        outList.append(x[index])
        del overlap[index]
        del x[index]

    #If the ordered list is the same as the initial list, the initial list was ordered
    if j == outList:
        result.append(outList)

#Make a list of the middle numbers
midNums = [int(x[len(x)//2]) for x in result]

print(sum(midNums))