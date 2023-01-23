with open("9.in") as f:
    lines = [l.strip() for l in f]

H = (5, 0)
T = [(5, 0) for _ in range(9)]
p1 = set()
p2 = set()
DR = {"R": 0, "L": 0, "U": -1, "D": 1}
DC = {"R": 1, "L": -1, "U": 0, "D": 0}


def displayAllTail(H, T):
    rows, cols = (6, 6)
    for row in range(rows):
        for col in range(cols):
            if row == H[0] and col == H[1]:
                print("H", end="")
            else:
                for i in range(0, len(T)):
                    if row == T[i][0] and col == T[i][1]:
                        print(i + 1, end="")
                        break
                else:
                    print(".", end="")
        print()


def displayTail(H, T):
    rows, cols = (6, 6)
    for row in range(rows):
        for col in range(cols):
            if row == H[0] and col == H[1]:
                print("H", end="")
            elif row == T[0] and col == T[1]:
                print("#", end="")
            else:
                print(".", end="")
        print()


def displayTailTrace(H, T):
    R = [r for r, c in T]
    C = [c for r, c in T]
    maxR, minR = max(R), min(R)
    maxC, minC = max(C), min(C)
    print(T)
    for row in range(minR - 1, maxR + 2):
        for col in range(minC - 2, maxC + 4):
            if row == H[0] and col == H[1]:
                print("H", end="")
            else:
                for r, c in T:
                    if row == r and col == c:
                        print("#", end="")
                        break
                else:
                    print(".", end="")
        print()


def move(H, T):
    dr = H[0] - T[0]
    dc = H[1] - T[1]

    if abs(dr) >= 2 and abs(dc) >= 1 or abs(dr) >= 1 and abs(dc) >= 2:
        T = (
            T[0] + 1 if H[0] > T[0] else T[0] - 1,
            T[1] + 1 if H[1] > T[1] else T[1] - 1,
        )
    elif abs(dr) >= 2:
        T = (T[0] + 1 if H[0] > T[0] else T[0] - 1, T[1])
    elif abs(dc) >= 2:
        T = (T[0], T[1] + 1 if H[1] > T[1] else T[1] - 1)
    return T


for l in lines:
    d, amt = l.split()
    for _ in range(int(amt)):
        H = (H[0] + DR[d], H[1] + DC[d])
        T[0] = move(H, T[0])
        for i in range(1, len(T)):
            T[i] = move(T[i - 1], T[i])
        # displayTail(H, T[0])
        p1.add(T[0])
        p2.add(T[8])
print(len(p1))
print(len(p2))
displayTailTrace(H, p2)
