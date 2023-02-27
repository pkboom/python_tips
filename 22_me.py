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
    return {
        (4, 0): (6, 3-y, 0, 1),
        (5, 1): (2, x, 3,3)
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
                print(x, y)
                if t == ".":
                    nx, ny = x, y
                    dc += 1
                    t = M[(y + r) % R][(x + c) % C]
                    if (y + r == R or x + c == C or t == " ") and part == 2:
                        # get current region and coord
                        # convert it to new coord in new region
                        # move
                        # convert it back to general coord
                        region,nx, ny = getRegionAndCoord(x, y)
                        print("x,y,region,ny,ny: ", x,y,region,nx,ny) 
                        region, nx, ny,d = getNewRegionAndCoord(region, nx, ny, d)
                        print("region, nx,ny,d: ",region, nx,ny,d) 
                        x, y = convertToOldCoord(region, nx, ny) 
                        print("x,y,d: ",x,y,d) 
                        # new code for this region
                        # step forward
                        # convert to general coord
                elif t == "#":
                    x, y = nx, ny
                    break
            step = ""
        i += 1
    return 1000 * (y + 1) + 4 * (x + 1) + d


# print(solve(1))
print(solve(2))
# print(1000 * (y + 1) + 4 * (x + 1) + D.index(move))
