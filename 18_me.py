from collections import deque

lines = open("18.in").read().strip()

P = []
for line in lines.split("\n"):
    x, y, z = [int(coor) for coor in line.split(",")]
    P.append((x, y, z))


OUT = set()
IN = set()


def reach_outside(x, y, z, part):
    if (x, y, z) in OUT:
        return True
    if (x, y, z) in IN:
        return False
    if (x, y, z) in P:
        return False
    if part == 1:
        OUT.add((x, y, z))
        return True
    else:
        Q = deque([(x, y, z)])
        SEEN = set()
        while Q:
            x, y, z = Q.popleft()
            if (x, y, z) in OUT:
                continue
            if (x, y, z) in P:
                continue
            SEEN.add((x, y, z))
            if len(SEEN) > 5000:
                # seen enough
                #   legit
                for p in SEEN:
                    OUT.add(p)
                return True

            Q.append(x + 1, y, z)
            Q.append(x - 1, y, z)
            Q.append(x, y + 1, z)
            Q.append(x, y - 1, z)
            Q.append(x, y, z + 1)
            Q.append(x, y, z - 1)
        # inside
        for p in SEEN:
            IN.add(p)
        return False


def solve(part):
    ans = 0
    for x, y, z in P:
        if reach_outside(x + 1, y, z, part):
            ans += 1
        if reach_outside(x - 1, y, z, part):
            ans += 1
        if reach_outside(x, y + 1, z, part):
            ans += 1
        if reach_outside(x, y - 1, z, part):
            ans += 1
        if reach_outside(x, y, z + 1, part):
            ans += 1
        if reach_outside(x, y, z - 1, part):
            ans += 1
    return ans


# print(solve(1))
print(solve(2))
