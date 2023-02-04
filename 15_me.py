sensors = []
beacons = []
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


(sx, sy) = sensors[6]

mx, my = 0, 0

empty = set()
# until we see a beacon
beacon_touched = False
while True:
    mx += 1
    print((sx - mx, sy + my), end=",")
    if (sx - mx, sy + my) in beacons:
        beacon_touched = True
    elif (sx - mx, sy + my) not in sensors:
        empty.add((sx - mx, sy + my))

    for mxx in range(-mx + 1, 1):
        my += 1
        for myy in range(-my, my + 1):
            print((sx + mxx, sy + myy), end=",")
            if (sx + mxx, sy + myy) in beacons:
                beacon_touched = True
            elif (sx + mxx, sy + myy) not in sensors:
                empty.add((sx + mxx, sy + myy))
    my = 0
    for mxx in range(mx - 1, 0, -1):
        my += 1
        for myy in range(-my, my + 1):
            print((sx + mxx, sy + myy), end=",")
            if (sx + mxx, sy + myy) in beacons:
                beacon_touched = True
            elif (sx + mxx, sy + myy) not in sensors:
                empty.add((sx + mxx, sy + myy))
    my = 0
    print((sx + mx, sy + my))
    if (sx + mx, sy + my) in beacons:
        beacon_touched = True
    elif (sx + mx, sy + my) not in sensors:
        empty.add((sx + mx, sy + my))
    if beacon_touched:
        break


print(empty)
# cx, cy = (sx - 1, sy)
# print(cx, cy)
min_x = min([x for x, _ in sensors] + ([x for x, _ in beacons]))
max_x = max([x for x, _ in sensors] + ([x for x, _ in beacons]))
min_y = min([y for _, y in sensors] + ([y for _, y in beacons]))
max_y = max([y for _, y in sensors] + ([y for _, y in beacons]))
print(min_x)
print(max_x)
print(min_y)
print(max_y)

for i in range(min_x - 3, max_x - 2):
    for j in range(min_y - 2, max_y + 4):
        if (j, i) in beacons:
            print("B", end="")
        elif (j, i) in sensors:
            print("S", end="")
        elif (j, i) in empty:
            print("#", end="")
        else:
            print(".", end="")
    print()
