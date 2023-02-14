from collections import deque

lines = open("19.in").read().strip().split("\n")

B = {}
for line in lines:
    b = [b.strip(":") for b in line.split(" ") if b.strip(":").isnumeric()]
    # ore, clay, obsidian(ore), obsidian(clay), geode(ore), geode(obsidian)
    B[b[0]] = (int(b[1]), int(b[2]), int(b[3]), int(b[4]), int(b[5]), int(b[6]))

R = []
total_geode = 0
for k, v in B.items():
    SEEN = set()
    geo_max = 0
    R.clear()
    t = 23
    Q = deque([(t, 1, 0, 0, 0, 1, 0, 0, 0)])
    while Q:
        t, m0, m1, m2, m3, r0, r1, r2, r3 = Q.popleft()
        if (t, m0, m1, m2, m3, r0, r1, r2, r3) in SEEN:
            continue
        if t < 20:
            SEEN.add((t, m0, m1, m2, m3, r0, r1, r2, r3))
        if t < 1:
            if geo_max < m3:
                geo_max = m3
            continue
        if m0 >= v[4] and m2 >= v[5]:
            Q.append(
                (
                    t - 1,
                    m0 - v[4] + r0,
                    m1 + r1,
                    m2 - v[5] + r2,
                    m3 + r3,
                    r0,
                    r1,
                    r2,
                    r3 + 1,
                )
            )
            continue
        if m0 >= v[2] and m1 >= v[3]:
            Q.append(
                (
                    t - 1,
                    m0 - v[2] + r0,
                    m1 - v[3] + r1,
                    m2 + r2,
                    m3 + r3,
                    r0,
                    r1,
                    r2 + 1,
                    r3,
                )
            )
            continue
        if m0 >= v[1]:
            Q.append(
                (
                    t - 1,
                    m0 - v[1] + r0,
                    m1 + r1,
                    m2 + r2,
                    m3 + r3,
                    r0,
                    r1 + 1,
                    r2,
                    r3,
                )
            )
        if m0 >= v[0]:
            Q.append(
                (
                    t - 1,
                    m0 - v[0] + r0,
                    m1 + r1,
                    m2 + r2,
                    m3 + r3,
                    r0 + 1,
                    r1,
                    r2,
                    r3,
                )
            )
        Q.append((t - 1, m0 + r0, m1 + r1, m2 + r2, m3 + r3, r0, r1, r2, r3))
    total_geode += geo_max * int(k)
print(total_geode)
