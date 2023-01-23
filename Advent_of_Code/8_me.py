with open("8.in") as f:
    lines = [l.strip() for l in f]

R = len(lines)
C = len(lines[0])


p1 = 0
for r in range(R):
    for c in range(C):
        t = lines[r][c]
        visible = False
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rr = r
            cc = c
            while True:
                rr = rr + dr
                cc = cc + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if t <= lines[rr][cc]:
                        break
                else:
                    visible = True
                    p1 += 1
                    break
            if visible:
                break


print(p1)

p2 = 0
for r in range(R):
    for c in range(C):
        score = 1
        t = lines[r][c]
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rr = r
            cc = c
            v = 1
            while True:
                rr = rr + dr
                cc = cc + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if t <= lines[rr][cc]:
                        score *= v
                        break
                else:
                    score *= v - 1
                    break
                v += 1
        p2 = max(p2, score)


print(p2)
