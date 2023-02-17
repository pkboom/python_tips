from collections import deque

lines = open("example.in").read().strip().split("\n")
# lines = open("20.in").read().strip().split("\n")

S = []
M = []
for line in lines:
    S.append(int(line))
    M.append(int(line))

length = len(S)
c = 0
p1 = 0
p2 = 0
while True:
    if c == 1000:
        print(M)
        print(M[(M.index(0) + 1) % length])
        p1 += M[(M.index(0) + 1) % length]
    if c == 2000:
        print(M)
        print(M[(M.index(0) + 1) % length])
        p1 += M[(M.index(0) + 1) % length]
    if c == 3000:
        print(M)
        print(M[(M.index(0) + 1) % length])
        p1 += M[(M.index(0) + 1) % length]
        break
    current = S[c % len(S)]
    print(c % len(S))
    m_key = M.index(current)
    if m_key + current > length:
        m_new_key = m_key + current + 1
    elif m_key + current < 0:
        m_new_key = m_key + current - 1
    else:
        m_new_key = m_key + current

    m_new_key = m_new_key % length

    if m_new_key >= m_key:
        step = 1
    else:
        step = -1

    for i in range(m_key, m_new_key, step):
        M[i % length], M[(i + step) % length] = M[(i + step) % length], M[i % length]
    c += 1

print(p1)
