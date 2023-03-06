from collections import deque
from copy import deepcopy

# lines = open("25.in").read().strip().split("\n")
lines = open("example.in").read().strip().split('\n')

SNAFU =[] 
for line in lines:
    SNAFU.append(line.strip())

to_dec = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }
dec = 0
while SNAFU:
    n = SNAFU.pop()
    p = 1
    dec = to_dec[n[-1]]
    for nn in range(len(n) - 2, -1, -1):
        p *= 5
        dec += (to_dec[n[nn]] * p)
    # print('dec',dec)

lines = open("decimal.in").read().strip().split('\n')

DECIMAL =[] 
for line in lines:
    DECIMAL.append(line.strip())


to_fiv = {
    ('1', '1'): '2',
}
fiv = 0
DECIMAL = DECIMAL[::-1] 
print(DECIMAL)
while DECIMAL:
    n = DECIMAL.pop()
    print('n', n)
    q = int(n)
    fiv = ''
    c = 1
    while True:
        q, r = q // 5, q % 5
        print('q,r',q,r)
        if r == 1:
            if len(fiv) == c:
                fiv = to_fiv[('1', fiv[0])] + fiv[1:]
            else :
                fiv = '1' + fiv
        elif r == 2:
            if len(fiv) == c:
                fiv = to_fiv[('1', fiv[0])] + fiv[1:]
            else :
                fiv = '2' + fiv
        elif r == 0:
            fiv = '0' + fiv
        elif r == 3:
            fiv = '1=' + fiv
        elif r == 4:
            fiv = '1-' + fiv
        print('fiv',fiv)
        print('-' * 20)
        if q == 0:
            break
        c += 1
    if n == '20':
        quit()
quit()

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

