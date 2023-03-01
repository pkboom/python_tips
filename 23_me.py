from collections import deque

lines = open("23.in").read().strip().split("\n")
lines = open("example.in").read().strip().split("\n")

E = deque() # elves positions
for j, line in enumerate(lines):
    for i, l in enumerate(line):
        if l == '#':
            E.append((i,j))
elves = len(E)

# move each elf
mc = 0 # move counter
# simulate an elf
P = [
    ((-1,-1), (0,-1), (1,-1)),
    ((1,1), (0,1), (-1,1)), 
    ((-1,1), (-1,0), (-1,-1)),
    ((1,-1), (1,0), (1,1)),
]
old_positions = deque()
new_positions = deque()
# check surrounding tiles: 
for _ in range(4):
    for ex,ey in E:
        for dx, dy in ((-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)):
            nx, ny = ex + dx, ey + dy
            if (nx,ny) in E: 
                print("(ex,ey) (nx,ny)", (ex,ey), (nx,ny))
                # search for a new position
                break
        else:
            print("elf", (ex,ey), "is no elves around it")
            new_positions.append((ex,ey))
            break
    
        # search for a new position
        mmc = mc % 4
        for i in range(mc, mc+4):
            # search one line
            side = P[i % 4]
            for dx, dy in side :
                nx, ny = ex + dx, ey + dy
                if (nx,ny) in E:
                    break
            else:
                # we have an empty line
                new_positions.append((ex + side[1][0], ey+side[1][1]))
                break
        else:
            print((ex,ey), "surrounded by elves")
            new_positions.append((ex,ey))
    
    mc += 1
    
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
    for j in range(y_min, y_max+1):
        a = ''
        for i in range(x_min, x_max+1):
            if (i,j) in E:
                a += '#'
            else:
                a += '.'
        print(a)


print(E)
print(new_positions)
new_positions.clear()
quit()




# # if there is no elf, do nothing
# # if this is an elf, next proposal.

# quit()
# d = ((-1,-1),(0,-1),(1,-1))
# d = ((-1,-1),(0,-1),(1,-1))
# d = ((-1,-1),(0,-1),(1,-1))
# d = ((-1,-1),(0,-1),(1,-1))
# instr = lines[-1]
# r = len(m)
# c = max(len(x) for x in m)
# cube = c // (4 if example else 3)
# for r in range(r):
#     while len(m[r]) < c:
#         m[r] += " "
#     assert len(m[r]) == c, (len(m[r]), c)
# d = ((1, 0), (0, 1), (-1, 0), (0, -1))

