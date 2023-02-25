from collections import deque

# lines = open("example.in").read().split("\n\n")
lines = open("22.in").read().split("\n\n")

M = [line for line in lines[:-1][0].split("\n")]
instr = lines[-1]
R = len(M)
C = max(len(x) for x in M)
CUBE = C // 4
for x in range(R):
    while len(M[x]) < C:
        M[x] += " "
    assert len(M[x]) == C, (len(M[x]), C)
D = ((1, 0), (0, 1), (-1, 0), (0, -1))


def getDirection(t, d):
    if t == "R":
        return (d + 1) % 4
    elif t == "L":
        return (d + 3) % 4
    assert False, (t, d)


# .12
# .3.
# 45.
# 6

REGION = ((1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3))


def getRegionAndCoord(x, y):
    for i in range(len(REGION)):
        xx, yy = REGION[i]
        if CUBE * xx <= x < CUBE * (xx + 1) and CUBE * yy <= y < CUBE * (yy + 1):
            return (i + 1, CUBE * xx + x, CUBE * yy + y)

    # if CUBE * 1 <= x < CUBE * 2 and CUBE * 0 <= y < CUBE * 1 :
    # region 1
    # if CUBE * 2 <= x < CUBE * 3 and CUBE * 0 <= y < CUBE * 1 :
    # region 2
    # if CUBE * 1 <= x < CUBE * 2 and CUBE * 1 <= y < CUBE * 2 :
    # region 3
    # if CUBE * 0 <= x < CUBE * 1 and CUBE * 2 <= y < CUBE * 3 :
    # region 4
    # if CUBE * 1 <= x < CUBE * 2 and CUBE * 2 <= y < CUBE * 3 :
    # region 5
    # if CUBE * 0 <= x < CUBE * 1 and CUBE * 3 <= y < CUBE * 4 :
    # region 6
    # get current region
    # using d, get new region and new d
    # using new region and new d, get new coord
    #


def solve(part):
    d = 0
    i = 0
    step = ""
    x, y = 0, 0
    for m in M[0]:
        if m == " ":
            x += 1
    while i < len(instr):
        if instr[i] == "R" or instr[i] == "L":
            d = getDirection(instr[i], d)
            print("Turn", d)
        else:
            step += instr[i]
        if i == len(instr) - 1 or instr[i + 1] == "R" or instr[i + 1] == "L":
            c, r = D[d]
            dc = 0
            while dc < int(step):
                y = (y + r) % R
                x = (x + c) % C
                t = M[y][x]
                print(x, y)
                if t == " " and part == 2:
                    nx, ny = getRegionAndCoord(x, y)
                    # new code for this region
                    # step forward
                    # convert to general coord
                    pass
                if t == ".":
                    nx, ny = x, y
                    dc += 1
                elif t == "#":
                    x, y = nx, ny
                    break
            step = ""
        i += 1
    return 1000 * (y + 1) + 4 * (x + 1) + d


# print(solve(1))
print(solve(2))
# print(1000 * (y + 1) + 4 * (x + 1) + D.index(move))
