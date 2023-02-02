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

all_open = 1
for valve in dist["AA"]:
    all_open = all_open | bitmask[valve]
print(all_open)
for valve, distance in dist.items():
    print(valve, distance)
time = 30
pressures = []
for valve, distance in dist["AA"].items():
    queue = [
        (time - distance, valve, bitmask[valve] | bitmask["AA"], 0)
    ]  # time, valve, bit, pressure
    while queue:
        time, current, b, pressure = queue.pop()
        if time <= 0 or b & all_open == all_open:
            pressures.append(pressure)
            print(current, time, pressure)
            continue
        p = (time - 1) * rates[current]
        for t in dist[current].keys():
            if b & bitmask[t] == 0:
                queue.append(
                    (time - 1 - dist[current][t], t, b | bitmask[t], p + pressure)
                )

print(max(pressures))
