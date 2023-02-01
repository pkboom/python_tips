from copy import deepcopy

with open("16.in") as f:
    lines = [l.strip() for l in f]

S = {}
b = 1
all_open = 0
for l in lines:
    scan = l.split()
    v, r, t = scan[1], int(scan[4][5:-1]), [_.strip(",") for _ in scan[9:]]
    S[v] = [r, t, b]  # rate, tunnel
    print(v, S[v])
    all_open |= b
    b <<= 1

Q = [
    [0, "AA", 0, 0, "AA", ""]
]  # count, current value, pressure, open, path, duplicate path
M = 0

while len(Q) > 0:
    c, v, p, open, path, duplicate = Q.pop()
    if (open & all_open) == all_open:
        M = max(M, p)
        continue
    if c >= 30:
        M = max(M, p)
        continue

    for t in S[v][1]:
        if path + t == duplicate:
            M = max(M, p)
            continue
        if t in path:
            duplicate = path
            path = ""
        Q.append([c + 1, t, p, open | S[v][2], path + t, duplicate])
        if (S[v][2] & open) == 0 and S[v][0] != 0:
            Q.append(
                [
                    c + 2,
                    t,
                    p + S[v][0] * (30 - (c + 1)),
                    open | S[v][2],
                    path + t,
                    duplicate,
                ]
            )

print(M)
