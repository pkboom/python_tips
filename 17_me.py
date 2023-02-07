from collections import deque

D = open("17.in").read().strip()

R = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0000100, 0b0000100, 0b0011100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000],
]

L = [len(l) for l in R]

C1 = [0b1111111]
C2 = []


def draw_chamber():
    for i in range(len(C1)):
        print(
            bin(
                (C1[i] | C2[0][i - C2[1]])
                if C2[1] <= i < (C2[1] + len(C2[0]))
                else C1[i]
            )[2:].rjust(7, "0")
        )
    print("=================================")


def move(d):
    R2 = []
    for l in range(len(C2[0])):
        part_of_rock = C2[0][l]
        if d == "<":
            new_r = part_of_rock * 2
            # left wall
            if new_r & 0b10000000:
                return
        else:
            new_r = part_of_rock // 2
            # right wall
            if part_of_rock & 1:
                return
        #  overlap with existing rock?
        if C1[C2[1] + l] & new_r:
            return
        R2.append(new_r)
    for l in range(len(C2[0])):
        C2[0][l] = R2[l]


def down():
    for l in range(len(C2[0])):
        if C1[C2[1] + 1 + l] & C2[0][l]:
            # hit bottom, you stop
            # move rock from C2 to C1
            for l in range(len(C2[0])):
                C1[C2[1] + l] |= C2[0][l]
            return True
    else:
        # move down
        C2[1] += 1
        return False


rc = 0
dc = 0
while True:
    # put rock in chamber2
    C2 = [R[rc % 4].copy(), 0]
    for i in range(3 + len(R[rc % 4])):
        if C1[i] != 0:
            C1.insert(0, 0b0000000)
    while True:  # start moving, if hit bottom, stop
        d = D[dc]  # direction
        draw_chamber()
        move(d)
        draw_chamber()
        # down
        if down():
            break
        draw_chamber()
        dc += 1
    rc += 1
