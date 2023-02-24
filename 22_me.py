from collections import deque

lines = open("example.in").read().split("\n\n")
# lines = open("22.in").read().split("\n\n")

map = [line for line in lines[:-1][0].split("\n")]
path = lines[-1]
m_h = len(map)
m_w = max([len(line) for line in map])
move = (1, 0)
D = ((1, 0), (0, 1), (-1, 0), (0, -1))


def get_direction(d):
    return D[(D.index(move) + 1) % 4] if d == "R" else D[(D.index(move) - 1) % 4]


i = 0
step = ""
p = [0, 0]  # x, y
while i < len(path):
    if path[i] == "R" or path[i] == "L":
        move = get_direction(path[i])
    else:
        step += path[i]
    if i == len(path) - 1 or path[i + 1] == "R" or path[i + 1] == "L":
        c, r = move
        dc = 0
        while dc < int(step):
            p[1] = (p[1] + r) % m_h
            p[0] = (p[0] + c) % m_w
            try:
                t = map[p[1]][p[0]]
            except:
                continue
            if t == ".":
                x_tile, y_tile = p
                dc += 1
            elif t == "#":
                p = [x_tile, y_tile]
                break
        step = ""
    i += 1

print(p)
x, y = p
x += 1
y += 1
print(1000 * y + 4 * x + D.index(move))
