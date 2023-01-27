from collections import defaultdict, deque

with open("12.in") as f:
    lines = [l.strip() for l in f]

G = []
for line in lines:
    G.append(line)
R = len(G)
C = len(G[0])

E = [[0 for _ in range(C)] for _ in range(R)]

Q = deque()
for i in range(R):
    for j in range(C):
        if G[i][j] == "E":
            E[i][j] = 26
        elif G[i][j] == "S":
            Q.append(((i, j), 0))
            E[i][j] = 1
        else:
            E[i][j] = ord(G[i][j]) - ord("a") + 1

S = set()
while True:
    (r, c), d = Q.popleft()
    if (r, c) in S:
        continue
    S.add((r, c))
    if G[r][c] == "E":
        print(d)
        break
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        rr = dr + r
        cc = dc + c
        if 0 <= rr < R and 0 <= cc < C and E[r][c] + 1 >= E[rr][cc]:
            Q.append(((rr, cc), d + 1))
