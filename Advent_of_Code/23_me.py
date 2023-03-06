from collections import deque
from copy import deepcopy

lines = open("23.in").read().strip().split("\n")
# lines = open("example.in").read().strip().split("\n")

E = set()
for j, line in enumerate(lines):
    for i, l in enumerate(line):
        if l == '#':
            E.add((i,j))

c = 0 # move counter
P = [
    ((-1,-1), (0,-1), (1,-1)),
    ((1,1), (0,1), (-1,1)), 
    ((-1,1), (-1,0), (-1,-1)),
    ((1,-1), (1,0), (1,1)),
]
nextP = set()
newP = []
oldP = deque()

while True:
    if c == 10:
        x_max = max(x for x, _ in E)
        x_min = min(x for x, _ in E)
        y_max = max(y for _, y in E)
        y_min = min(y for _, y in E)

        y_val = y_max - y_min + 1
        x_val = x_max - x_min + 1
        print(x_val * y_val - len(E)) 

    for ex,ey in E:
        for dx, dy in ((-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)):
            nx, ny = ex + dx, ey + dy
            if (nx, ny) in E: 
                # search for a new position
                break
        else:
            # no elves around it
            nextP.add((ex,ey))
            continue
    
        for i in range(c, c+4):
            side = P[i % 4]
            for dx, dy in side :
                nx, ny = ex + dx, ey + dy
                if (nx,ny) in E:
                    break
            else:
                # print('(ex, ey) (dx, dy), (nx, ny)', (ex, ey), side[1], (ex + side[1][0], ey+side[1][1]))
                newP.append((ex + side[1][0], ey + side[1][1]))
                oldP.append((ex,ey))
                break
        else:
            # surrounded by elves
            nextP.add((ex,ey))
    
    if c % 100 == 0:
        print('c', c)
    if E == nextP:
        print("no change", c + 1)
        break
    
    for np in newP:
        op = oldP.popleft()
        if newP.count(np) > 1:
            # duplicate new positions
            nextP.add(op) 
        else:
            nextP.add(np) 
   
    assert len(oldP) == 0, oldP 

    c += 1
    E = deepcopy(nextP)
    newP.clear()
    nextP.clear()

