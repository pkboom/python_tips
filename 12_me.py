from copy import deepcopy

with open("12.in") as f:
    lines = [l.strip() for l in f]

for l in lines:
    print(l)

r_len = len(lines)
c_len = len(lines[0])


def move(r, c, r_len, c_len, history):
    print("history", history)
    rr = r + 1
    cc = c + 1

    if rr >= r_len or cc >= c_len:
        history.append((r, c, "X"))
        return history

    print(lines[r][c])
    print(lines[rr][c])
    print(lines[r][cc])

    if lines[r][c] == "c":
        history.append((r, c, "V"))
        return history

    if 0 <= (ord(lines[rr][c]) - ord(lines[r][c])) <= 1:
        history.append((r, c, "V"))
        return move(rr, c, r_len, c_len, history)
    if 0 <= (ord(lines[r][cc]) - ord(lines[r][c])) <= 1:
        history.append((r, c, ">"))
        return move(r, cc, r_len, c_len, history)


r = 0
c = 0

h = move(r, c, r_len, c_len, [])
print(h)
