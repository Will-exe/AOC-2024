aList = []
count = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(' ')
        aList.append(parts)
'''
def is_increasing_ok(a):
    return all(1 <= int(a[i+1]) - int(a[i]) <= 3 for i in range(len(a) - 1))

def is_decreasing_ok(a):
    return all(1 <= int(a[i]) - int(a[i+1]) <= 3 for i in range(len(a) - 1))
'''

for x in aList:
    if all(1 <= abs(int(x[i]) - int(x[i+1])) <= 3 for i in range(len(x) - 1)):
        count += 1
        


print(count)