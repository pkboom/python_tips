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


y = 10
# y = 2000000
empty = set()
# empty = 0
for i, (sx, sy) in enumerate(sensors):
    # (sx, sy) = sensors[6]
    beacon_touched = False
    mx, my = 0, 0
    while True:
        mx += 1
        # print((sx - mx, sy), end=",")
        if (sx - mx, sy) == beacons[i]:
            beacon_touched = True
        elif (sx - mx, sy) not in sensors:
            if sy == y:
                empty.add((sx - mx, sy))

        for mxx in range(-mx + 1, 1):
            my += 1
            if (sx + mxx, sy - my) == beacons[i]:
                beacon_touched = True
            elif (sx + mxx, sy - my) not in sensors:
                if sy - my == y:
                    empty.add((sx + mxx, sy - my))
            if (sx + mxx, sy + my) == beacons[i]:
                beacon_touched = True
            elif (sx + mxx, sy + my) not in sensors:
                if sy + my == y:
                    empty.add((sx + mxx, sy + my))

        my = 0
        for mxx in range(mx - 1, 0, -1):
            my += 1
            # print((sx + mxx, sy + myy), end=",")
            if (sx + mxx, sy + my) == beacons[i]:
                beacon_touched = True
            elif (sx + mxx, sy + my) not in sensors:
                if sy + my == y:
                    empty.add((sx + mxx, sy + my))
            if (sx + mxx, sy - my) == beacons[i]:
                beacon_touched = True
            elif (sx + mxx, sy - my) not in sensors:
                if sy - my == y:
                    empty.add((sx + mxx, sy - my))
        my = 0
        # print((sx + mx, sy + my))
        if (sx + mx, sy + my) == beacons[i]:
            beacon_touched = True
        elif (sx + mx, sy + my) not in sensors:
            if sy + my == y:
                empty.add((sx + mx, sy + my))
        if beacon_touched:
            break

# min_x = min([x for x, _ in sensors] + ([x for x, _ in beacons]))
# max_x = max([x for x, _ in sensors] + ([x for x, _ in beacons]))
# min_y = min([y for _, y in sensors] + ([y for _, y in beacons]))
# max_y = max([y for _, y in sensors] + ([y for _, y in beacons]))
# for j in range(min_y, max_y + 1):
#     print(j, end="")
#     for i in range(min_x - 2, max_x + 2):
#         if (i, j) in beacons:
#             print("B", end="")
#         elif (i, j) in sensors:
#             print("S", end="")
#         elif (i, j) in empty:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
# for x, y in empty:
#     if y == 2000000:
#         c += 1
print(len(empty))
# print(empty)
