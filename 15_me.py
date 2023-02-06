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
for x in range(min_x - 3000000, max_x + 3000000):
    # for x in range(min_x - 30, max_x + 30):
    if (x, y) in beacons:
        continue
    if (x, y) in sensors:
        continue
    for i, (sx, sy) in enumerate(sensors):
        if abs(x - sx) + abs(y - sy) <= dist[i]:
            c += 1
            break
print(c)
