from collections import defaultdict, deque

with open("13.in") as f:
    lines = [l.strip() for l in f.read().split("\n\n")]

D = []
for line in lines:
    D.append([eval(_) for _ in line.split("\n")])


def check_in_order(l, r):
    c = min(len(l), len(r))
    for cc in range(c):
        if isinstance(l[cc], list) and isinstance(r[cc], list):
            if not check_in_order(l[cc], r[cc]):
                return False
            else:
                continue
        while isinstance(l[cc], list) and isinstance(r[cc], int):
            if isinstance(l[cc], list) and len(l[cc]) == 0:
                return True
            l[cc] = l[cc][0]
        while isinstance(l[cc], int) and isinstance(r[cc], list):
            if isinstance(r[cc], list) and len(r[cc]) == 0:
                return False
            r[cc] = r[cc][0]
        if l[cc] < r[cc]:
            return True
        else:
            return False

    if len(l) > len(r):
        return False

    return True


in_order = []
for i, d in enumerate(D):
    print("-" * 20)
    l, r = d
    print(l)
    print(r)
    if check_in_order(l, r):
        in_order.append(i + 1)


print("in_order", in_order)
print(sum(in_order))
