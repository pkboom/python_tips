with open("10.in") as f:
    lines = [l.strip() for l in f.read().strip().split("\n")]

r = 1
c = 0
signal = 0
crt = [[0 for _ in range(40)] for _ in range(6)]
sprite = [0, 1, 2]


def get_signal(c, r, signal, crt):
    c += 1
    cr, cc = (c - 1) // 40, (c - 1) % 40
    crt[cr][cc] = "#" if cc in sprite else "."
    return signal + (c * r if (c - 20) % 40 == 0 else 0), crt, c


for l in lines:
    signal, crt, c = get_signal(c, r, signal, crt)
    if l == "noop":
        continue
    signal, crt, c = get_signal(c, r, signal, crt)
    _, n = l.split()
    r += int(n)
    sprite = [(r % 40) - 1, (r % 40), (r % 40) + 1]

print(signal)
for _ in crt:
    print("".join(_))
