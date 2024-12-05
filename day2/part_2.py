aList = []
count = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(' ')
        aList.append(parts)




for x in aList:
    if all(1 <= int(x[i]) - int(x[i+1]) <= 3 for i in range(len(x) - 1)) or all(1 <= int(x[i+1]) - int(x[i]) <= 3 for i in range(len(x) - 1)):
        count += 1
    else:
        for j in range(len(x)):
            poppedNum = x.pop(j)
            if all(1 <= int(x[i]) - int(x[i+1]) <= 3 for i in range(len(x) - 1)) or all(1 <= int(x[i+1]) - int(x[i]) <= 3 for i in range(len(x) - 1)):
                count += 1
                break
            else:
                x.insert(j, poppedNum)
            
        


print(count)