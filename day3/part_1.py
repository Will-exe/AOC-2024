import re
from functools import reduce

aList = []
count = 0

with open('input.txt', 'r') as file:
    txt = file.read()

regexPattern = r"mul\(\d{1,3},\d{1,3}\)"


out = re.findall(regexPattern, txt)

for x in out:
    x = x[4:-1]
    x = re.split(',',x)
    count += reduce(lambda x,y: x*y, (int(i) for i in x))
    
print(count)
