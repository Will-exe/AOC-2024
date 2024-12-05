
a1 = []
a2 = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split('   ')
        a1.append(int(parts[0]))
        a2.append(int(parts[1]))

a1.sort()
a2.sort()

dist = []

for x in range(len(a1)):
    dist.append(abs(a1[x] - a2[x]))

print("sum dist :", sum(dist))

amtDict = {}
for x in a1:
    amtDict[x] = a2.count(x)

score = 0
for x in a1:
    score += x * amtDict[x]
print(score)