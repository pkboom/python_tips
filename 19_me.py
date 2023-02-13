from collections import deque
from copy import deepcopy

lines = open("19.in").read().strip().split("\n")

B = {}
for line in lines:
    i, orrc, crc, obrc1, obrc2, grc1, grc2 = [
        b.strip(":") for b in line.split(" ") if b.strip(":").isnumeric()
    ]
    B[i] = {
        "orrc": int(orrc),
        "crc": int(crc),
        "obrc": (int(obrc1), int(obrc2)),
        "grc": (int(grc1), int(grc2)),
    }
    print(B)

for k, v in B.items():
    t = 24
    Q = deque([([0, 0, 0, 0], [1, 0, 0, 0])])
    while t > 0:
        ((m0, m1, m2, m3), (r0, r1, r2, r3)) = Q.popleft()
        m0 += r0  # add ore
        Q.append(((m0, m1, m2, m3), (r0, r1, r2, r3)))
        if m0 >= v["orrc"]:
            # keep digging or
            m0 -= v["orrc"]
            r0 += 1
            Q.append(((m0, m1, m2, m3), (r0, r1, r2, r3)))
            # create ore robot and dig
        t -= 1
