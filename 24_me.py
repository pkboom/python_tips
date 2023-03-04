from collections import deque
from copy import deepcopy

lines = open("24.in").read().strip().split("\n")
# lines = open("example.in").read().strip().split("\n")

start = [i for i, l in enumerate(lines[0]) if l == '.']
start = (start[0], 0)

exit = [i for i, l in enumerate(lines[-1]) if l == '.']
exit = (exit[0], len(lines)-1)

print('start', start)
print('exit', exit)
D = {
    '>': (1,0),
    '<': (-1,0),
    '^': (0,-1),
    'v': (0,1),
}

blizzard = []
directions = []
for j, line in enumerate(lines[1:-1]):
    for i, l in enumerate(line):
        if l != '#' and l != '.':
            blizzard.append((i, j+1))
            directions.append(D[l])

E = deque([start])
cc = 0
while True:
    # move blizzard 
    c = 0
    while c < len(blizzard):
        x, y= blizzard[c]
        dx, dy= directions[c]
        nx, ny = x + dx, y + dy
        if nx < 1:
            nx = len(lines[0]) - 2
        elif nx > len(lines[0]) - 2:
            nx = 1
        if ny < 1:
            ny = len(lines) - 2
        elif ny > len(lines) - 2:
            ny = 1
        blizzard[c] = (nx, ny)
        directions[c] = (dx, dy)
        c += 1
    cc += 1


    # start expedition
    cache = set()
    print('cache', cache)
    print('E', E)
    while E:
        ex, ey = E.popleft() 
        if (ex, ey) in blizzard:
            continue
        # search four directions
        for dx, dy in ((-1,0),  (0,-1),  (1,0),  (0,1)):
            nx, ny = ex + dx, ey + dy
            # if (nx, ny) in blizzard: 
            #     # blizzard 
            #     continue
            if (nx < 1 or nx > len(lines[0]) - 2 or ny < 1 or ny > len(lines) - 2) and (nx, ny) != exit: 
                # hit wall 
                continue
            # move
            cache.add((nx, ny))
            # print(nx, ny)
        else:
            cache.add((ex, ey))
    E = deque(cache)
    print('E', E)
    if exit in cache:
        print('arrived', cc + 1)
        break

    # for j in range(len(lines)):
    #     map = '' 
    #     for i in range(len(lines[0])):
    #         if (i,j) in blizzard:
    #             map += [k for k, v in D.items() if v == directions[blizzard.index((i,j))]][0]
    #         elif (i,j) in E:
    #             map += 'E'
    #         elif i < 1 or i > len(lines[0]) - 2 or j < 1 or j > len(lines) - 2: 
    #             map += '#'
    #         else:
    #             map += '.'
    #     print(map)
    
    # if cc == 19:
    #     quit()
