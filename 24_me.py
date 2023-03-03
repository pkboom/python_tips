from collections import deque
from copy import deepcopy

# lines = open("24.in").read().strip().split("\n")
lines = open("example.in").read().strip().split("\n")

start = [i for i, l in enumerate(lines[0]) if l == '.']
start = (start[0], 0)

exit = [i for i, l in enumerate(lines[-1]) if l == '.']
exit = (exit[0], len(lines)-1)

D = {
    '>': (1,0),
    '<': (-1,0),
    '^': (0,-1),
    'v': (0,1),
}

blizzard = []
for j, line in enumerate(lines[1:-1]):
    for i, l in enumerate(line):
        if l != '#' and l != '.':
            blizzard.append(((i, j+1), D[l]))
print(blizzard)
E = deque(start)
cc = 0
while True:
    # move blizzard 
    c = 0
    while c < len(blizzard):
        (x, y), (dx, dy) = blizzard[c]
        nx, ny = x + dx, y + dy
        if nx < 1:
            nx = len(lines[0]) - 2
        elif nx > len(lines[0]) - 2:
            nx = 1
        if ny < 1:
            ny = len(lines) - 2
        elif ny > len(lines) - 2:
            ny = 1
        blizzard[c] = ((nx, ny), (dx, dy))
        c += 1
    cc += 1

    # start expedition
    # search four directions
    # if empty, move. 
    print(blizzard)
    if cc == 10:
        quit()

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

