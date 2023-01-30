with open("16.in") as f:
    lines = [l.strip() for l in f]

S = {}
for l in lines:
    scan = l.split()
    v, r, t = scan[1], int(scan[4][5:-1]), [_.strip(",") for _ in scan[9:]]
    S[v] = [r, t]  # rate, tunnel

Q = [0, "AA", 0]  # count, valve, points
M = 0
q = []
total = 0
O = []

while True:
    c, v, p = Q
    # if c >= 30 or all_open:
    #     M = max(M, p)
    #     print(len(Q), M)
    #     continue
    if v not in O:
        O.append(v)

        bigger = False
        for vv in S[v][1]:
            if vv not in O and S[v][0] < S[vv][0]:
                bigger = True
                break
        if not bigger and S[v][0] != 0:
            c += 1
            p += S[v][0] * (30 - c)
        MAX = 0
        next = ""
        for vv in S[v][1]:
            sum = 0
            for vvv in S[vv][1]:
                if vvv in O:
                    continue
                sum += S[vvv][0]
            if S[vv][0] + sum >= MAX:
                MAX = S[vv][0] + sum
                next = vv
        Q = [c + 1, next, p]


print(M)
