keys = []
vals = []

class treeNode:
    def __init__(self, sum = None,op = None, left = None, right = None, parent = None, depth = 0):
        self.parent = parent
        self.sum = sum
        self.op = op
        self.left = left
        self.right = right
        self.depth = depth

    def eval(self, x, y):
        return self.op(x, y)
    
    def expand_left(self, x):
        if not self.left:
            newSum = mul(x, self.sum)
            self.left = treeNode(op = "mul", sum = newSum, depth = self.depth+1, parent = self)
    
    def expand_right(self, x):
        if not self.right:
            newSum = add(x, self.sum)
            self.right = treeNode(op = "add", sum = newSum, depth = self.depth+1, parent = self)
    
    def getParent(self):
        return self.parent
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getSum(self):
        return self.sum
    
    def __str__(self):
        print()
        print("Operation: ", self.op)
        print("Val: ", self.sum)
        print("Depth: ", self.depth)


with open('pinput.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        key, values = line.strip().split(':')
        keys.append(int(key.strip()))
        vals.append(values.split())


vals = [[int(i) for i in x] for x in vals]

def add(x,y):
    return x + y

def mul(x,y):
    return x * y


currentNodes = []
newNodes = []
totalSum = 0


for key in range(len(keys)):
    print(key)
    if vals[key][0] < keys[key]:
        root = treeNode(sum = vals[key][0], depth=0)
        currentNodes.append(root)
    else:
        continue
        

    for val in range(1, len(vals[key])):
        newNodes = []
        for node in currentNodes:
            if vals[key][val] * node.getSum() < keys[key]:
                node.expand_left(vals[key][val])
                newNodes.append(node.getLeft())
            if vals[key][val] + node.getSum() < keys[key]:
                node.expand_right(vals[key][val])
                newNodes.append(node.getRight())
            
        currentNodes = newNodes
    for node in currentNodes:
        try:
            print("key: ", keys[key])
            print(node)
        except TypeError as e:
            continue
        if node.getSum() == keys[key]:
            totalSum += keys[key]
            print(totalSum)
            break



        
"""
try:
            print("key: ", keys[key])
            print(node)
        except TypeError as e:
            continue
"""
print(keys)
print(vals)