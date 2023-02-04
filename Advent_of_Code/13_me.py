from copy import deepcopy

with open("13.in") as f:
    lines = [l.strip() for l in f.read().split("\n\n")]

D = []
for line in lines:
    D.append([eval(_) for _ in line.split("\n")])
S = []
for d1, d2 in D:
    S.append(d1)
    S.append(d2)


def check_in_order(l, r):
    c = min(len(l), len(r))
    for cc in range(c):
        if isinstance(l[cc], int) and isinstance(r[cc], int):
            if l[cc] == r[cc]:
                continue
            return l[cc] < r[cc]
        if isinstance(r[cc], int):
            r[cc] = [r[cc]]
        if isinstance(l[cc], int):
            l[cc] = [l[cc]]
        result = check_in_order(l[cc], r[cc])
        if result == "equal":
            continue
        return result

    return "equal" if len(l) == len(r) else len(l) < len(r)


in_order = []
for i, d in enumerate(D):
    l, r = d
    if check_in_order(l, r):
        in_order.append(i + 1)

S.append([2])
S.append([6])
for i in range(0, len(S) - 1):
    for j in range(i + 1, len(S)):
        if not check_in_order(deepcopy(S[i]), deepcopy(S[j])):
            S[i], S[j] = S[j], S[i]

print(sum(in_order))
print((S.index([2]) + 1) * (S.index([6]) + 1))
