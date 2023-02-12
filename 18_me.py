lines = open("18.in").read().strip()

P = []
for line in lines.split("\n"):
    x, y, z = [int(coor) for coor in line.split(",")]
    P.append((x, y, z))


def reach_outside(x, y, z):
    if (x, y, z) in P:
        return False
    return True


ans = 0
for x, y, z in P:
    print(x, y, z)
    if reach_outside(x + 1, y, z):
        ans += 1
    if reach_outside(x - 1, y, z):
        ans += 1
    if reach_outside(x, y + 1, z):
        ans += 1
    if reach_outside(x, y - 1, z):
        ans += 1
    if reach_outside(x, y, z + 1):
        ans += 1
    if reach_outside(x, y, z - 1):
        ans += 1

print(ans)
