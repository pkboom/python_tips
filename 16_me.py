from collections import deque

rates = {}
tunnels = {}
bitmask = {}
for b, line in enumerate(open("16.in")):
    scan = line.split()
    v, r, t = scan[1], int(scan[4][5:-1]), [_.strip(",") for _ in scan[9:]]
    rates[v] = int(r)
    tunnels[v] = t
    bitmask[v] = 1 << b

dist = {}
for valve, rate in [r for r in rates.items() if r[1] != 0 or r[0] == "AA"]:
    dist[valve] = {}
    queue = deque([(valve, valve, bitmask[valve], 0)])
    while queue:
        origin, current, b, distance = queue.popleft()
        for t in tunnels[current]:
            if b & bitmask[t] != 0:
                continue
            if t in dist[origin]:
                continue
            if rates[t] != 0:
                dist[origin][t] = distance + 1
            queue.append((origin, t, b | bitmask[t], distance + 1))

all_open = bitmask["AA"]
for valve in dist["AA"]:
    all_open = all_open | bitmask[valve]

cache = {}


def get_max_pressure(valve, distance, b):
    if b & all_open == all_open:
        return 0
    if (valve, distance, b) in cache:
        return cache[(valve, distance, b)]
    pressure = 0
    if rates[valve] != 0:
        distance -= 1
        pressure = distance * rates[valve]

    sum = [0]
    for v, d in dist[valve].items():
        if v == "AA":
            continue
        if b & bitmask[v] != 0:
            continue
        if distance - d <= 0:
            continue
        sum.append(get_max_pressure(v, distance - d, bitmask[v] | b))
    cache[(valve, distance, b)] = pressure + max(sum)
    return pressure + max(sum)


print(get_max_pressure("AA", 30, bitmask["AA"]))
