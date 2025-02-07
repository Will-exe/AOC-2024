import re
from sympy import Eq, symbols, solve

#Button A: X+94, Y+34
#Button B: X+22, Y+67
#Prize: X=8400, Y=5400


pattern = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\n"
    r"Button B: X\+(\d+), Y\+(\d+)\n"
    r"Prize: X=(\d+), Y=(\d+)\n?"
)

data = []
with open('input.txt', 'r') as file:
    txt = file.read().strip()

for match in pattern.finditer(txt):
    Ax, Ay, Bx, By, Lx, Ly = map(int, match.groups())
    data.append([[Ax,Ay],[Bx,By],[Lx,Ly]])

sols = []

n, k = symbols('n k', integer=True)
for data in data:
    eq1 = Eq(n*data[0][0] + k*data[1][0], data[2][0])
    eq2 = Eq(n*data[0][1] + k*data[1][1], data[2][1])

    sols.append(solve((eq1,eq2), (n,k), dict=True))


val = 0
for sol in sols:
    print(sol)
    if len(sol) == 0:
        continue
    elif len(sol) > 1:
        bestCost = 0
        cost = 0
        for opts in sol:
            cost = opts[n]*3 + opts[k]
            if cost < bestCost: bestCost = cost
            cost = 0
        val += bestCost
    else:
        val += sol[0][n]*3 + sol[0][k]

print(val)
#print(txt)
#print(data)
#for sol in sols:
#    print(sol)
#print(sols)