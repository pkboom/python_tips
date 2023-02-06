sensors = []
beacons = set()
for line in open("15.in"):
    data = line.split()
    sx, sy, bx, by = (
        int(data[2][2:-1]),
        int(data[3][2:-1]),
        int(data[8][2:-1]),
        int(data[9][2:]),
    )
    d = abs(sx - bx) + abs(sy - by)
    sensors.append((sx, sy, d))
    beacons.add((bx, by))


def valid(x, y):
    for sx, sy, d in sensors:
        if abs(sx - x) + abs(sy - y) <= d:
            return False
    return True


for sx, sy, d in sensors:
    for dx in range(d + 2):
        dy = d + 1 - dx
        # print(dx, dy)
        for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x = sx + dx * signx
            y = sy + dy * signy
            if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                continue
            assert abs(sx - x) + abs(sy - y) == d + 1
            if valid(x, y):
                print(x, y)
                print(x * 4000000 + y)
