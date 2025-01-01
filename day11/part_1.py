from functools import *

with open('input.txt', 'r') as file:
    txt = file.read().strip().split(' ')

#test = ['125', '17']
#txt = test

k = 25



for j in range(k):

    i = 0
    while i < len(txt):
        if txt[i] == '0': 
            txt[i] = '1'
            i += 1
            continue
        if len(txt[i]) > 1 and len(txt[i]) % 2 == 0:
            k = len(txt[i]) // 2
            right = str(int(txt[i][k:]))
            left = str(int(txt[i][:k]))
            txt[i] = left
            txt.insert(i+1, right)
            i += 2
            continue
        else:
            txt[i] = str(int(txt[i]) * 2024)
            i += 1
            continue


"""

@cache
def processList(ls):
    i = 0
    while i < len(ls):
        if ls[i] == '0': 
            ls[i] = '1'
            i += 1
            continue
        if len(ls[i]) > 1 and len(ls[i]) % 2 == 0:
            k = len(ls[i]) // 2
            right = str(int(ls[i][k:]))
            left = str(int(ls[i][:k]))
            ls[i] = left
            ls.insert(i+1, right)
            i += 2
            continue
        else:
            ls[i] = str(int(ls[i]) * 2024)
            i += 1
            continue
    print(ls)
    return ls

for j in range(k):
    print(len(txt))
    txt = processList(txt)
    

"""
print(len(txt))