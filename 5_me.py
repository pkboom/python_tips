with open("5.in") as f:
    X = [l for l in f.read().split("\n\n")]

stacks = []
stacks2 = []

for i in X[0].split("\n")[-1].split(None):
    stacks.append([])
    stacks2.append([])

for j in X[0].split("\n")[:-1]:
    for m in range(len(stacks)):
        if j[m * 4 + 1] != " ":
            stacks[m].append(j[m * 4 + 1].strip())
            stacks2[m].append(j[m * 4 + 1].strip())

for i in X[1].split("\n"):
    a = i.split(" ")
    number = int(a[1])
    x = int(a[3]) - 1
    y = int(a[5]) - 1

    for n in range(number):
        stacks[y].insert(0, stacks[x].pop(0))

    for q in reversed(stacks2[x][:number]):
        stacks2[y].insert(0, q)
    stacks2[x] = stacks2[x][number:]

print("".join([s[0] for s in stacks if len(s) > 0]))
print("".join([s[0] for s in stacks2 if len(s) > 0]))
