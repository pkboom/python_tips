from collections import deque

M = open("17.in").read().strip()

R = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0000100, 0b0000100, 0b0011100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000],
]

C = [0b0000000, 0b0000000, 0b0000000, 0b1111111]


def draw_chamber():
    for i in C:
        print(bin(i)[2:].rjust(7, "0"))


def move(d):
    # right wall, left wall, or overlap with top of bottom
    if c == "<":
        return C[0] * 2
    else:
        return C[0] // 2


# a rock appears at top
# first move
# down
# it can go down 3 without hitting bottom
c = 0
while True:
    print(c)
    m = M[c]
    print(m)
    for i in range(len(R[c % 4])):
        C.pop(0)
    for i in range(len(R[c % 4]) - 1, -1, -1):
        C.insert(0, R[c % 4][i])
    draw_chamber()
    # move first
    C[0] = move(c)
    # before move: does it hit wall or previous rock
    draw_chamber()
    # down
    C.pop(1)
    C.insert(0, 0b0000000)
    draw_chamber()
    # move
    C[0] = move(c)
    draw_chamber()
    C.pop(2)
    C.insert(0, 0b0000000)
    draw_chamber()
    c += 1
