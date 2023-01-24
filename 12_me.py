from copy import deepcopy

with open("12.in") as f:
    lines = [l.strip() for l in f]

H = []
P = []
x = 0
y = 0
r_len = len(lines)
c_len = len(lines[0])
h = [(x, y)]
hp = []
prev = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p = ["V", ">", "^", "<"]
found_e = False

while True:
    next = ()

    for i, dd in enumerate(d):
        r, c = dd
        rr, cc = x + r, y + c

        if rr < 0 or cc < 0 or rr >= r_len or cc >= c_len:
            continue

        if (rr, cc) in h:
            continue

        h_copied = deepcopy(h)
        h_copied.append((rr, cc))
        if h_copied in prev:
            continue

        if (ord(lines[rr][cc]) - ord(lines[x][y])) == 1:
            next = (rr, cc)
            break

        if lines[rr][cc] == "E":
            break

        if not next and (ord(lines[rr][cc]) - ord(lines[x][y])) <= 0:
            next = (rr, cc)
            continue

    print("next", next)
    print("prev", prev)
    if found_e and lines[rr][cc] == "E":
        steps = deepcopy(h)
        H.append(steps)
        print("steps", steps)
        print("-------------------------------")

    if next:
        x, y = next
        if lines[x][y] == "e":
            found_e = True
        h.append((x, y))
        print("history", h)
        print("x, y", x, y)
        print("character", lines[x][y])
    else:
        prev.append(deepcopy(h))
        h.pop()
        if len(h) == 0:
            break
        x, y = h[-1]
        print("backward x, y", x, y)
        print("backward history", h)


print("H", H)
