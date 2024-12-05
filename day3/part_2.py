import re
from functools import reduce

aList = []
count = 0

with open('input.txt', 'r') as file:
    txt = file.read()

regexPattern = r"mul\(\d{1,3},\d{1,3}\)"
excludePattern = r"don't\(\)(.*?)(do\(\)?)"

excludedTxt = re.sub(excludePattern, "", txt)
print(excludedTxt)
out = re.findall(regexPattern, excludedTxt)

for x in out:
    x = x[4:-1]
    x = re.split(',',x)
    count += reduce(lambda x,y: x*y, (int(i) for i in x))
    
print(count)
