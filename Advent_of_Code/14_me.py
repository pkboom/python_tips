with open("14.in") as f:
    lines = [l.strip() for l in f]

R = []
for l in lines:
    ll = [_ for _ in l.split("->")]
    for i in range(len(ll) - 1):
        x1, y1 = ll[i].strip().split(",")
        x2, y2 = ll[i + 1].strip().split(",")
        for i in range(int(min(x1, x2)), int(max(x1, x2)) + 1):
            for j in range(int(min(y1, y2)), int(max(y1, y2)) + 1):
                R.append((i, j))
max_x, max_y = max([x for x, _ in R]), max([y for _, y in R])
min_x, min_y = min([x for x, _ in R]), min([y for _, y in R])
print(min_x, max_x, min_y, max_y)


S = []


def move(x, y):
    if y == max_y:
        return x, y
    for d in [(0, 1), (-1, 1), (1, 1)]:
        if (x + d[0], y + d[1]) not in R and (x + d[0], y + d[1]) not in S:
            return move(x + d[0], y + d[1])
    return x, y


while True:
    x, y = move(500, 0)
    if y == max_y:
        break
    S.append((x, y))

for y in range(0, max_y + 1):
    for x in range(min_x - 1, max_x + 2):
        if (x, y) in R:
            print("#", end="")
        elif (x, y) in S:
            print("o", end="")
        else:
            print(".", end="")
    print()
print(len(S))
