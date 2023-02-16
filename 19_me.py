from collections import deque


def solve(Co, Cc, Co1, Co2, Cg1, Cg2, T):
    best = 0
    SEEN = set()
    Q = deque([(0, 0, 0, 0, 1, 0, 0, 0, T)])
    Core = max(Co, Cc, Co1, Cg1)
    while Q:
        state = Q.popleft()
        o, c, ob, g, r0, r1, r2, r3, t = state

        if t == 0:
            best = max(best, g)
            continue

        if r0 > Core:
            r0 = Core
        if r1 > Co2:
            r1 = Co2
        if r2 > Cg2:
            r2 = Cg2
        if o > Core * t - r0 * (t - 1):
            o = Core * t - r0 * (t - 1)
        if c > Co2 * t - r1 * (t - 1):
            c = Co2 * t - r1 * (t - 1)
        if ob > Cg2 * t - r2 * (t - 2):
            ob = Cg2 * t - r2 * (t - 2)

        state = (o, c, ob, g, r0, r1, r2, r3, t)
        if state in SEEN:
            continue
        SEEN.add(state)

        if len(SEEN) % 1000000 == 0:
            print(t, len(SEEN))
        Q.append((o + r0, c + r1, ob + r2, g + r3, r0, r1, r2, r3, t - 1))
        if o >= Co:
            Q.append((o - Co + r0, c + r1, ob + r2, g + r3, r0 + 1, r1, r2, r3, t - 1))
        if o >= Cc:
            Q.append((o - Cc + r0, c + r1, ob + r2, g + r3, r0, r1 + 1, r2, r3, t - 1))
        if o >= Co1 and c >= Co2:
            Q.append(
                (o - Co1 + r0, c - Co2 + r1, ob + r2, g + r3, r0, r1, r2 + 1, r3, t - 1)
            )
        if o >= Cg1 and ob >= Cg2:
            Q.append(
                (o - Cg1 + r0, c + r1, ob - Cg2 + r2, g + r3, r0, r1, r2, r3 + 1, t - 1)
            )
    return best


p1 = 0
p2 = 1
lines = open("example.in").read().strip().split("\n")
# lines = open("19.in").read().strip().split("\n")
for line in lines:
    id_, ore, clay, ob_ore, ob_clay, g_ore, g_ob = [
        int(b.strip(":")) for b in line.split(" ") if b.strip(":").isnumeric()
    ]
    s1 = solve(ore, clay, ob_ore, ob_clay, g_ore, g_ob, 24)
    p1 += s1 * id_
    if id_ > 3:
        continue
    s2 = solve(ore, clay, ob_ore, ob_clay, g_ore, g_ob, 32)
    p2 *= s2
print(p1)
print(p2)
