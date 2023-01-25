from copy import deepcopy

with open("12.in") as f:
    lines = [l.strip() for l in f]

H = []
P = []
x = 0
y = 0
r_len = len(lines)
c_len = len(lines[0])
hp = []
prev = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p = ["V", ">", "^", "<"]
found_e = False


def move(x, y, h=[]):
    next = [[], [], [], []]

    for i, dd in enumerate(d):
        r, c = dd
        rr, cc = x + r, y + c

        if rr < 0 or cc < 0 or rr >= r_len or cc >= c_len:
            continue

        if (rr, cc) in h:
            continue

        if (ord(lines[rr][cc]) - ord(lines[x][y])) == 1:
            next[i] = move(rr, cc, h + [(rr, cc)])
        elif lines[rr][cc] == "E":
            return h + [(rr, cc)]
        elif (ord(lines[rr][cc]) - ord(lines[x][y])) <= 0:
            next[i] = move(rr, cc, h + [(rr, cc)])

    next = [n for n in next if n]
    if not next:
        return []
    l = 99999
    key = 0
    for i, n in enumerate(next):
        if len(n) < l:
            l = len(n)
            key = i

    return next[key]


path = move(x, y, [(x, y)])

print("path", path)
