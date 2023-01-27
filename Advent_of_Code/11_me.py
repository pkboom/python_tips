with open("11.in") as f:
    lines = [l.strip() for l in f.read().strip().split("\n\n")]

I = []
M = [[], []]
OP = []
DIV = []
TRUE = []
FALSE = []

for l in lines:
    _, items, op, test, true, false = l.split("\n")
    M[0].append([int(i.strip()) for i in (items.split(":")[-1].split(","))])
    M[1].append([int(i.strip()) for i in (items.split(":")[-1].split(","))])
    words = op.split()
    op = "".join(words[-3:])
    OP.append(lambda old, op=op: eval(op))
    DIV.append(int(test.split(" ")[-1]))
    TRUE.append(int(true.split(" ")[-1]))
    FALSE.append(int(false.split(" ")[-1]))

lcm = 1
for k in DIV:
    lcm = lcm * k

for j, _ in enumerate([range(20), range(10000)]):
    I = [0 for ___ in range(len(M[j]))]
    for __ in _:
        for i, m in enumerate(M[j]):
            for item in m:
                item = OP[i](item)
                if j == 1:
                    item %= lcm
                else:
                    item = item // 3
                if item % DIV[i] == 0:
                    M[j][TRUE[i]].append(item)
                else:
                    M[j][FALSE[i]].append(item)
                I[i] += 1
            M[j][i] = []

    print("p{}: {}".format(j + 1, sorted(I)[-1] * sorted(I)[-2]))
