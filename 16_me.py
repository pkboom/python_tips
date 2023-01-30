from collections import deque
from copy import deepcopy

with open("16.in") as f:
    lines = [l.strip() for l in f]

S = {}
for l in lines:
    scan = l.split()
    v, r, t = scan[1], int(scan[4][5:-1]), [_.strip(",") for _ in scan[9:]]
    S[v] = [r, t]  # rate, tunnel

Q = [[0, "AA", 0, False]]
M = 0
q = []

while len(Q) > 0:
    c, v, p, all_open, *open = Q.pop()
    if c >= 30 or all_open:
        M = max(M, p)
        print(len(Q), M)
        continue
    if v not in open:
        open = open + [v]
        if S[v][0] != 0:
            c += 1
            p += S[v][0] * (30 - c)
        if len(open) == len(S):
            all_open = True

    for t in S[v][1]:
        Q.append([c + 1, t, p, all_open, *open])

print(M)
