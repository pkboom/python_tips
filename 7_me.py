with open("7.in") as f:
    lines = [l.strip() for l in f.readlines()]

d = {}

for l in lines:
    if l.startswith("$ cd"):
        dir = l[5:]

        if dir == "/":
            cwd = "/"
        elif dir == "..":
            cwd = cwd[: cwd[:-1].rfind("/")] + "/"
        else:
            cwd = cwd + dir + "/"

        if cwd not in d:
            d[cwd] = {}

    elif l.startswith("$ ls"):
        continue

    else:
        size, name = l.split()

        if size == "dir":
            d[cwd][name] = "dir"
        else:
            d[cwd][name] = size

s = {}

for key, value in d.items():
    total = 0
    for m, n in value.items():
        if n != "dir":
            total += int(n)

    s[key] = total

for key, value in d.items():
    for m, n in value.items():
        if n == "dir":
            s[key] += sum([s2 for s1, s2 in s.items() if s1.startswith(key + m)])


total_size = sum([v for k, v in s.items() if v < 100000])
print(total_size)

used = s["/"]
free = 70000000 - used
required = min([v for k, v in s.items() if v > (30000000 - free)])
print(required)
