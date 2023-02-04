with open("14.in") as f:
    lines = [l.strip() for l in f]

R = set()
for l in lines:
    ll = [_ for _ in l.split("->")]
    for i in range(len(ll) - 1):
        x1, y1 = ll[i].strip().split(",")
        x2, y2 = ll[i + 1].strip().split(",")
        for i in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
            for j in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
                R.add((i, j))


max_x, max_y = max([x for x, _ in R]), max([y for _, y in R])
min_x, min_y = min([x for x, _ in R]), min([y for _, y in R])
print(min_x, max_x, min_y, max_y)
S = set()

for x in range(min_x - 1000, max_x + 1000):
    R.add((x, max_y + 2))

for i, bottom in enumerate([max_y, max_y + 2]):
    while True:
        sx, sy = 500, 0
        while sy != bottom:
            for d in [(0, 1), (-1, 1), (1, 1)]:
                if (sx + d[0], sy + d[1]) not in R and (sx + d[0], sy + d[1]) not in S:
                    sx, sy = sx + d[0], sy + d[1]
                    break
            else:
                S.add((sx, sy))
                break
        if sy == bottom or (sx, sy) == (500, 0):
            print(len(S))
            break


# for y in range(0, max_y + 1):
#     for x in range(min_x - 1, max_x + 2):
#         if (x, y) in R:
#             print("#", end="")
#         elif (x, y) in S:
#             print("o", end="")
#         else:
#             print(".", end="")
#     print()

# for y in range(0, max_y + 3):
#     for x in range(min_x - 20, max_x + 20):
#         if (x, y) in R:
#             print("#", end="")
#         elif (x, y) in S:
#             print("o", end="")
#         else:
#             print(".", end="")
#     print()
