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
        size, name = X[i].split()

        if name in cwd:
            continue

        if size == "dir":
            cwd[name] = {}
        else:
            cwd[name] = size


print(d)


def print_dict(d, path):
    total = 0
    y = 0

    for key, value in d.items():
        print(path, key, value)
        if type(value) is dict:
            if not value:
                continue
            x, y = print_dict(value, path + key + "/")
        else:
            total += int(value)

    if y > 0:
        return [(path, total + y)] + x, total + y
    else:
        return [(path, total)], total


asdf, asdf2 = print_dict(d["/"], "/")
print(asdf)
