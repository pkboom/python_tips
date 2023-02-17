from collections import deque

D = open("17.in").read().strip()
LD = len(D)
R = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0000100, 0b0000100, 0b0011100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000],
]
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
            if new_r & 0b10000000:
                return
        else:
            new_r = part_of_rock // 2
            if part_of_rock & 1:
                return
        if C1[C2[1] + l] & new_r:
            return
        R2.append(new_r)
    for l in range(len(C2[0])):
        C2[0][l] = R2[l]


def down():
    for l in range(len(C2[0])):
        if C1[C2[1] + 1 + l] & C2[0][l]:
            for l in range(len(C2[0])):
                C1[C2[1] + l] |= C2[0][l]
            return True
    else:
        C2[1] += 1
        return False


def get_direction(dc):
    return D[dc % LD]


p1 = 2022
p2 = 1000000000000
rc = 0
dc = 0
height = 0
while True:
    C2 = [R[rc % len(R)].copy(), 0]
    for i in range(len(C1)):
        if C1[i] != 0:
            break
    # if rc == p1:
    if rc == p2:
        print(len(C1) - i - 1)
        break
    if i <= len(R[rc % len(R)]) + 2:
        for _ in range(len(R[rc % len(R)]) + 3 - i):
            C1.insert(0, 0b0000000)
    else:
        for _ in range(i - (3 + len(R[rc % len(R)]))):
            C1.remove(0)
    while True:
        d = get_direction(dc)
        move(d)
        dc = (dc + 1) % LD
        # dc += 1
        # draw_chamber()
        if down():
            break
        # draw_chamber()
    rc += 1
