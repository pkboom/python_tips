from collections import deque

example = True
# example = False
if example:
    lines = open("example.in").read().split("\n\n")
else:
    lines = open("22.in").read().split("\n\n")

M = [line for line in lines[:-1][0].split("\n")]
instr = lines[-1]
R = len(M)
C = max(len(x) for x in M)
CUBE = C // (4 if example else 3)
for r in range(R):
    while len(M[r]) < C:
        M[r] += " "
    assert len(M[r]) == C, (len(M[r]), C)
D = ((1, 0), (0, 1), (-1, 0), (0, -1))


def getDirection(t, d):
    if t == "R":
        return (d + 1) % 4
    elif t == "L":
        return (d + 3) % 4
    assert False, (t, d)

if example:
    # ..1.
    # 234.
    # ..56
    REGION = ((2, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2)) # for example
else:
    # .12
    # .3.
    # 45.
    # 6
    REGION = ((1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3)) # for 22


def getRegionAndCoord(x, y):
    for i in range(len(REGION)):
        xx, yy = REGION[i]
        if CUBE * xx <= x < CUBE * (xx + 1) and CUBE * yy <= y < CUBE * (yy + 1):
            return [i + 1, x - (CUBE * xx), y - (CUBE * yy)]

#  1   1
# 234 462
#  5   5

#  1   1
# 346 623
#  5   5 

#  4   4
# 613 356
#  2   2
def getNewRegionAndCoord(r, x, y, d):
    # return region, x, y, d
    len = CUBE - 1 
    return {
        (4, 0): (6, len-y, 0, 1),
        (5, 1): (2, len-x, len, 3),
        (3, 3): (1, 0, x, 3)
    }[(r,d)]

def convertToOldCoord(r, x,y) :
    xx,yy = REGION[r-1]
    return x + (CUBE * xx), y + (CUBE * yy)

def solve(part):
    d = 0
    i = 0
    step = ""
    x, y = 0, 0
    for m in M[0]:
        if m != " ":
            break
        x += 1
    while i < len(instr):
        if instr[i] == "R" or instr[i] == "L":
            d = getDirection(instr[i], d)
            print("Turn", d)
        else:
            step += instr[i]
        if i == len(instr) - 1 or instr[i + 1] == "R" or instr[i + 1] == "L":
            dc = 0
            while dc < int(step):
                c, r = D[d]
                y = (y + r) % R
                x = (x + c) % C
                t = M[y][x]
                print(x, y, t)
                if t == ".":
                    nx, ny = x, y
                    dc += 1
                    t = M[(y + r) % R][(x + c) % C]
                    if (y + r == R or x + c == C or t == " ") and part == 2:
                        dc += 1
                        region,rx, ry = getRegionAndCoord(x, y)
                        print("x, y, region, ry, ry: ", x, y, region, rx, ry) 
                        region, rx, ry,d = getNewRegionAndCoord(region, rx, ry, d)
                        print("new region, rx, ry, d: ",region, rx, ry, d) 
                        x, y = convertToOldCoord(region, rx, ry) 
                        t = M[y][x]
                        print("x,y,d,t: ",x,y,d,t) 
                if t == "#":
                    x, y = nx, ny
                    break
            step = ""
        i += 1
    return 1000 * (y + 1) + 4 * (x + 1) + d


# print(solve(1))
print(solve(2))
