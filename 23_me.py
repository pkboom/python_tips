from collections import deque

lines = open("23.in").read().strip().split("\n")
# lines = open("example.in").read().strip().split("\n")


E = deque()
for j, line in enumerate(lines):
    for i, l in enumerate(line):
        if l == '#':
            E.append((i,j))
elves = len(E)

mc = 0 # move counter
P = [
    ((-1,-1), (0,-1), (1,-1)),
    ((1,1), (0,1), (-1,1)), 
    ((-1,1), (-1,0), (-1,-1)),
    ((1,-1), (1,0), (1,1)),
]
next_positions = deque()
new_positions = deque()

while True:
    if mc == 10:
        y_val = y_max - y_min + 1
        x_val = x_max - x_min + 1
        print(x_val * y_val - len(E)) 
        # print(empty)
        # break
    for ex,ey in E:
        for dx, dy in ((-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)):
            nx, ny = ex + dx, ey + dy
            if (nx, ny) in E: 
                # search for a new position
                break
        else:
            # print("elf", (ex,ey), "is no elves around it")
            new_positions.append((ex,ey))
            continue
    
        # search for a new position
        for i in range(mc, mc+4):
            # search one side 
            side = P[i % 4]
            for dx, dy in side :
                nx, ny = ex + dx, ey + dy
                if (nx,ny) in E:
                    break
            else:
                # found a new position
                # print('(ex, ey) (dx, dy), (nx, ny)', (ex, ey), side[1], (ex + side[1][0], ey+side[1][1]))
                new_positions.append((ex + side[1][0], ey + side[1][1]))
                break
        else:
            # print((ex,ey), "surrounded by elves")
            new_positions.append((ex,ey))
    
    if mc % 100 == 0:
        print('mc', mc)
    if E == new_positions:
        print("no change", mc + 1)
        break
    
    for np in new_positions:
        op = E.popleft()
        if new_positions.count(np) > 1:
            # print("we have duplicate new positions", np)
            E.append(op) 
        else:
            # print("new position", np) 
            E.append(np) 
    
    x_max = max(x for x, _ in E)
    x_min = min(x for x, _ in E)
    y_max = max(y for _, y in E)
    y_min = min(y for _, y in E)

    mc += 1
    new_positions.clear()

