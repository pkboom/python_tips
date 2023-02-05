sensors = []
beacons = []
dist = []
for line in open("15.in"):
    data = line.split()
    sx, sy, bx, by = (
        int(data[2][2:-1]),
        int(data[3][2:-1]),
        int(data[8][2:-1]),
        int(data[9][2:]),
    )
    sensors.append((sx, sy))
    beacons.append((bx, by))
    dist.append(abs(sx - bx) + abs(sy - by))

min_x = min([x for x, _ in sensors])
max_x = max([x for x, _ in sensors])
min_y = min([y for _, y in sensors])
max_y = max([y for _, y in sensors])

y = 2000000
y = 10
c = 0
# for x in range(min_x - 3000000, max_x + 3000000):
# for x in range(min_x - 30, max_x + 30):
#     if (x, y) in beacons:
#         continue
#     if (x, y) in sensors:
#         continue
#     for i, (sx, sy) in enumerate(sensors):
#         if abs(x - sx) + abs(y - sy) <= dist[i]:
#             c += 1
#             break
# print(c)

# for y in range(min_y, max_y + 1):
#     for x in range(min_x, max_x + 1):
#         for i, (sx, sy) in enumerate(sensors):
#             if abs(x - sx) + abs(y - sy) <= dist[i]:
#                 break
#         else:
#             print(x, y, x * 4000000 + y)

outside = set()
for i, (sx, sy) in enumerate(sensors):
    x = sx + dist[i]
    edge = set()
    queue = [(x, sy)]
    while queue:
        x, y = queue.pop()
        for mx, my in (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ):
            xx, yy = x + mx, y + my
            if (
                abs(xx - sx) + abs(yy - sy) > dist[i]
                and xx > 0
                and yy > 0
                and xx < 4000000
                and yy < 4000000
            ):
                outside.add((xx, yy))
                continue
            if (xx, yy) in edge:
                continue
            if abs(xx - sx) + abs(yy - sy) == dist[i]:
                edge.add((xx, yy))
                queue.append((xx, yy))

for x, y in outside:
    for i, (sx, sy) in enumerate(sensors):
        if abs(x - sx) + abs(y - sy) <= dist[i]:
            break
    else:
        print(x, y, x * 4000000 + y)
