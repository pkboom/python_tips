from collections import deque


def solve(Co, Cc, Co1, Co2, Cg1, Cg2, t):
    SEEN = set()
    best = 0
    Q = deque([(0, 0, 0, 0, 1, 0, 0, 0, t)])
    while Q:
        state = Q.popleft()
        o, c, ob, g, r0, r1, r2, r3, t = state
        if t == 0:
            best = max(best, g)
            continue

        if state in SEEN:
            continue
        SEEN.add(state)

        Q.append((t - 1, o + r0, c + r1, ob + r2, g + r3, r0, r1, r2, r3))
        if o >= Co:
            Q.append((t - 1, o - Co + r0, c + r1, ob + r2, g + r3, r0 + 1, r1, r2, r3))
        if o >= Cc:
            Q.append((t - 1, o - Cc + r0, c + r1, ob + r2, g + r3, r0, r1 + 1, r2, r3))
        if o >= Co1 and c >= Co2:
            Q.append(
                (t - 1, o - Co1 + r0, c - Co2 + r1, ob + r2, g + r3, r0, r1, r2 + 1, r3)
            )
        if o >= Cg1 and ob >= Cg2:
            Q.append(
                (t - 1, o - Cg1 + r0, c + r1, ob - Cg2 + r2, g + r3, r0, r1, r2, r3 + 1)
            )
    return best


lines = open("19.in").read().strip().split("\n")
for line in lines:
    id_, ore, clay, ob_ore, ob_clay, g_ore, g_ob = [
        int(b.strip(":")) for b in line.split(" ") if b.strip(":").isnumeric()
    ]

    best = solve(ore, clay, ob_ore, ob_clay, g_ore, g_ob, 24)
    quality_level = best * id_
