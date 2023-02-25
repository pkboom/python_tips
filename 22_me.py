from collections import deque

lines = open("example.in").read().split("\n\n")
lines = open("22.in").read().split("\n\n")

M = [line for line in lines[:-1][0].split("\n")]
instr = lines[-1]
R = len(M)
C = max(len(x) for x in M)
for x in range(R):
    while len(M[x]) < C:
        M[x] += " "
    assert len(M[x]) == C, (len(M[x]), C)
move = (1, 0)
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
# n_square = 4


def get_direction(d):
    return D[(D.index(move) + 1) % 4] if d == "R" else D[(D.index(move) - 1) % 4]


i = 0
step = ""
p = [0, 0]  # x, y
while i < len(instr):
    if instr[i] == "R" or instr[i] == "L":
        move = get_direction(instr[i])
    else:
        step += instr[i]
    if i == len(instr) - 1 or instr[i + 1] == "R" or instr[i + 1] == "L":
        c, r = move
        dc = 0
        while dc < int(step):
            p[1] = (p[1] + r) % R
            p[0] = (p[0] + c) % C
            t = M[p[1]][p[0]]
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
