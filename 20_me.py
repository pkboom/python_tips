from collections import deque

lines = open("example.in").read().strip().split("\n")
# lines = open("20.in").read().strip().split("\n")

S = []
M = []
for line in lines:
    S.append(int(line))
    M.append(int(line))

c = 0
p1 = 0
p2 = 0
while True:
    if c == 1000:
        print(M[(M.index(0) + 1) % len(M)])
        p1 += M[(M.index(0) + 1) % len(M)]
    if c == 2000:
        print(M[(M.index(0) + 1) % len(M)])
        p1 += M[(M.index(0) + 1) % len(M)]
    if c == 3000:
        print(M[(M.index(0) + 1) % len(M)])
        p1 += M[(M.index(0) + 1) % len(M)]
        break
    # get one number from S
    n = S[c % len(S)]
    m_key = M.index(n)
    m_new_key = m_key + n
    if m_new_key < 0:
        m_new_key = (m_new_key % len(M)) - 1
    else:
        m_new_key = m_new_key % len(M)

    c2 = 0
    while c2 < len(M):
        
    for i in range(m_key, len(M)):
        if (i % len(M)) == m_new_key:
            break
        M[i], M[i + 1] = M[i + 1], M[i]
    c += 1

print(p1)
