lines = open("18.in").read().strip().split("\n")

S = set()
Coor = []
for line in lines:
    x, y, z = [int(coor) for coor in line.split(",")]
    Coor.append((x, y, z))
    side = set()
    v = []
    for dx, dy, dz in [
        (0, 0, 0),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (-1, -1, 0),
        (0, -1, -1),
        (-1, 0, -1),
        (-1, -1, -1),
    ]:
        v.append((x + dx, y + dy, z + dz))
    side.add(frozenset((v[0], v[1], v[4], v[2])))  # up
    side.add(frozenset((v[0], v[2], v[5], v[3])))  # right
    side.add(frozenset((v[0], v[1], v[6], v[3])))  # back
    side.add(frozenset((v[7], v[4], v[1], v[6])))  # left
    side.add(frozenset((v[7], v[4], v[2], v[5])))  # front
    side.add(frozenset((v[7], v[6], v[3], v[5])))  # down
    S ^= side

print(len(S))
# print(Coor)
maxx = max([x for x, _, _ in Coor])
maxy = max([y for _, y, _ in Coor])
maxz = max([z for _, _, z in Coor])

for s in S:
    print(s)
    # ss0 = 0
    # ss1 = 0
    # ss2 = 0
    # for ss in s:
    #     print(ss)
    #     ss0 += ss[0]
    #     ss1 += ss[1]
    #     ss2 += ss[2]
