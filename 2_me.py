X = [l.strip() for l in open("2.in")]

total = 0
for x in X:
    op, me = x.split()
    p = {"X": 1, "Y": 2, "Z": 3}[me]
    p += {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }[(op, me)]

    total += p

    print(p)
print(total)
