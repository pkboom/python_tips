with open("1.in") as f:
    X = [l.strip() for l in f.read().split("\n\n")]
    print(X)

Q = []
for i in X:
    q = 0
    for j in i.split("\n"):
        q += int(j)
    Q.append(q)

print(max(Q))
print([Q.index(i) + 1 for i in Q if i == max(Q)])
