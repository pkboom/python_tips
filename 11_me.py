with open("11.in") as f:
    lines = [l.strip() for l in f.read().strip().split("\n\n")]

M = []
I = []

for l in lines:
    _, items, _ = l.split("\n")
    items = items.strip()[16:].split(", ")
    M.append(items)
    I.append(0)
    print(items)
    print(c.strip()[7:-1])
print(M, I)


for _ in range(20):
    for l in lines:
        ll = [ll.strip() for ll in l.split("\n")]
        m = int(ll[0][7:-1])
        for n in M[m]:
            o = int(n) if ll[2][23:] == "old" else int(ll[2][23:])
            yy = int(n) * o if ll[2][21] == "*" else int(n) + o
            w = yy // 3
            if w % int(ll[3][19:]) == 0:
                M[int(ll[4][25:])].append(w)
            else:
                M[int(ll[5][25:])].append(w)
            I[m] += 1
        M[m] = []

print("I", I)
print(sorted(I)[-1] * sorted(I)[-2])
print("M", M)
