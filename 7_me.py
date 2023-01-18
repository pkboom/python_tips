with open("7.in") as f:
    X = [l.strip() for l in f.readlines()]

d = {"/": {}}
h = []
cwd = []

for i in range(len(X)):
    if X[i].startswith("$ cd"):
        dir = X[i][5:]

        if dir == "/":
            h = ["/"]

        if dir == "..":
            h.pop()

        if dir in cwd:
            h.append(dir)

        print("hierarchy: ", h)
    elif X[i].startswith("$ ls"):
        cwd = d

        for h_ in h:
            cwd = cwd[h_]

        print("cwd", cwd)

    else:
        print(X[i])
        # if file, then add to dict
        size, name = X[i].split()

        if name in cwd:
            continue

        if size == "dir":
            cwd[name] = {}
        else:
            cwd[name] = size

print(d)
