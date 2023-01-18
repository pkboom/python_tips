with open("5.in") as f:
    X = [l for l in f.read().split("\n\n")]

stacks = []

for i in X[0].split("\n")[-1].split(None):
    stacks.append([])

for j in X[0].split("\n")[:-1]:
    c = 0
    for stack in stacks:
        stack.append(j[c * 4 + 1].strip())
        c += 1

c = 0
for stack in stacks:
    stacks[c] = list(filter(None, stack))
    c += 1

for i in X[1].split("\n"):
    a = i.split(" ")
    number = int(a[1])
    x = int(a[3]) - 1
    y = int(a[5]) - 1

    for n in range(number):
        stacks[y].insert(0, stacks[x].pop(0))

print(stacks)
