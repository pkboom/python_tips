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

D = { '>': (1,0), '<': (-1,0), '^': (0,-1), 'v': (0,1) }
b_pos = []
b_dir = []
for j, line in enumerate(lines[1:-1]):
    for i, l in enumerate(line):
        if l != '#' and l != '.':
            b_pos.append((i, j+1))
            b_dir.append(D[l])

w = len(lines[0])
h = len(lines)
E = deque([start])
cc = 0
p = 1
while True:
    # move blizzard 
    c = 0
    while c < len(b_pos):
        x, y= b_pos[c]
        dx, dy= b_dir[c]
        nx, ny = x + dx, y + dy
        if nx < 1:
            nx = w - 2
        elif nx > w - 2:
            nx = 1
        if ny < 1:
            ny = h - 2
        elif ny > h - 2:
            ny = 1
        b_pos[c] = (nx, ny)
        b_dir[c] = (dx, dy)
        c += 1
    cc += 1

    cache = set()
    while E:
        ex, ey = E.popleft() 
        if (ex, ey) in b_pos:
            continue
        for dx, dy in ((-1,0),  (0,-1),  (1,0),  (0,1)):
            nx, ny = ex + dx, ey + dy
            if (nx < 1 or nx > w - 2 or ny < 1 or ny > h - 2) and (nx, ny) != exit: 
                # hit wall 
                continue
            cache.add((nx, ny))
        else:
            cache.add((ex, ey))

    if exit in cache:
        print('arrived at exit({})'.format(p), cc + 1)
        if p == 3:
            break
        start, exit = exit, start
        E = deque([start])
        p += 1 
    else:
        E = deque(cache)

