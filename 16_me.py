from collections import deque

rates = {}
tunnels = {}
b = 1
for line in open("16.in"):
    scan = line.split()
    v, r, t = scan[1], int(scan[4][5:-1]), [_.strip(",") for _ in scan[9:]]
    rates[v] = r
    tunnels[v] = t
    # all_open |= b
    # b <<= 1

# caculate the distance from values to every other value with pressure
dist = {}
for valve, rate in rates.items():
    dist[valve] = {}
    print(valve, rate)
    queue = deque([(valve, valve, 0)])
    while queue:
        origin, current, distance = queue.popleft()
        for t in tunnels[current]:
            if t == "AA" or t in dist[origin]:
                continue
            # if rates[t] == 0:
            #     continue
            dist[origin][t] = distance + 1
            queue.append((origin, t, distance + 1))

# print(dist)
# b = 1
# all_open = 0
# for l in lines:

# Q = [
#     [0, "AA", 0, 0, "AA", ""]
# ]  # count, current value, pressure, open, path, duplicate path
# M = 0

# while len(Q) > 0:
#     c, v, p, open, path, duplicate = Q.pop()
#     if (open & all_open) == all_open:
#         M = max(M, p)
#         continue
#     if c >= 30:
#         M = max(M, p)
#         continue

#     for t in S[v][1]:
#         if path + t == duplicate:
#             M = max(M, p)
#             continue
#         if t in path:
#             duplicate = path
#             path = ""
#         Q.append([c + 1, t, p, open | S[v][2], path + t, duplicate])
#         if (S[v][2] & open) == 0 and S[v][0] != 0:
#             Q.append(
#                 [
#                     c + 2,
#                     t,
#                     p + S[v][0] * (30 - (c + 1)),
#                     open | S[v][2],
#                     path + t,
#                     duplicate,
#                 ]
#             )

# print(M)
