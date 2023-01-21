with open("9.in") as f:
    lines = [l.strip() for l in f]

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}

orientations = [
    (0, 0),
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

hr = 0
hc = 0
tr = 0
tc = 0

p1 = [(tr, tc)]
for l in lines:
    d, s = l.split()
    print("d, s:", d, s)

    for i in range(1, int(s) + 1):
        r, c = directions[d]
        print("i r c", i, r, c)
        hr = hr + r
        hc = hc + c
        print("hr hc tr tc", hr, hc, tr, tc)

        found = False
        for rr, cc in orientations:
            trr = tr + rr
            tcc = tc + cc
            if trr == hr and tcc == hc:
                print("found rr cc trr tcc", rr, cc, trr, tcc)
                diagonal = ()
                if rr * cc != 0:
                    print("diagonal", (rr, cc))
                    diagonal = (rr, cc)
                found = True
                break

        if found:
            continue

        if diagonal:
            print("diagonal", diagonal)
            r, c = diagonal

        tr = tr + r
        tc = tc + c
        p1.append((tr, tc))
        print("new tail", tr, tc)

print(set(p1))
print(len(set(p1)))
# add to P1 (0, 0)
# add to P1 (-1, 0)
# add to P1 (-1, 0)
# add to P1 (-2, 1)
# add to P1 (-2, 1)
# add to P1 (-2, 1)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 2)
# add to P1 (-2, 3)
# add to P1 (-2, 3)
# add to P1 (-2, 3)
# add to P1 (-2, 3)
# add to P1 (-2, 3)
# add to P1 (-2, 3)
# add to P1 (-3, 2)
# add to P1 (-4, 2)
# add to P1 (-4, 2)
# add to P1 (-4, 2)
# add to P1 (-4, 2)
# add to P1 (-3, 1)
# 8
# {(-3, 1), (0, 0), (-2, 1), (-1, 0), (-2, 3), (-4, 2), (-3, 2), (-2, 2)}
