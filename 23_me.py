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
new_positions = deque()

for _ in range(10):
    for ex,ey in E:
        for dx, dy in ((-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)):
            nx, ny = ex + dx, ey + dy
            if (nx, ny) in E: 
                # search for a new position
                break
        else:
            print("elf", (ex,ey), "is no elves around it")
            new_positions.append((ex,ey))
            continue
    
        # search for a new position
        mmc = mc % 4
        for i in range(mmc, mmc+4):
            # search one side 
            side = P[i % 4]
            for dx, dy in side :
                nx, ny = ex + dx, ey + dy
                if (nx,ny) in E:
                    break
            else:
                # we have an empty line
                print('(ex, ey) (dx, dy), (nx, ny)', (ex, ey), side[1], (ex + side[1][0], ey+side[1][1]))
                new_positions.append((ex + side[1][0], ey+side[1][1]))
                break
        else:
            # print((ex,ey), "surrounded by elves")
            new_positions.append((ex,ey))
    
    
    for _ in range(len(new_positions)):
        np = new_positions.popleft()
        op = E.popleft()
        if np in new_positions:
            print("we have duplicate new positions", np)
            new_positions.append(np)
            E.append(op) 
        else:
            print("new position", np) 
            E.append(np) 
    
    x_max = max(x for x, _ in E)
    x_min = min(x for x, _ in E)
    y_max = max(y for _, y in E)
    y_min = min(y for _, y in E)
    print(x_min, x_max, y_min, y_max)

    mc += 1
    new_positions.clear()
    empty = 0
    for j in range(y_min, y_max+1):
        a = ''
        for i in range(x_min, x_max+1):
            if (i,j) in E:
                a += '#'
            else:
                a += '.'
                empty += 1
        print(a)
    print('----------------------------')

print(empty)
