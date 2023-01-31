from collections import deque
from copy import deepcopy

with open("16.in") as f:
    lines = [l.strip() for l in f]

S = {}
for l in lines:
    scan = l.split()
    v, r, t = scan[1], int(scan[4][5:-1]), [_.strip(",") for _ in scan[9:]]
    S[v] = [r, t]  # rate, tunnel
    print(v, S[v])

Q = [[0, "AA", 0, [], []]]
M = 0
q = []

while len(Q) > 0:
    c, v, p, open, path = Q.pop()
    if c >= 30:
        M = max(M, p)
        print(len(Q), M)
        continue

    stuck = True
    for t in S[v][1]:
        if (v, t) not in path:
            Q.append([c + 1, t, p, open + [v], path + [(v, t)]])
            if v not in open and S[v][0] != 0:
                Q.append(
                    [
                        c + 2,
                        t,
                        p + S[v][0] * (30 - (c + 1)),
                        open + [v],
                        path + [(v, t)],
                    ]
                )
            stuck = False
    if stuck:
        M = max(M, p)

print(M)
