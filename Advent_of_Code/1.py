X = [l.strip() for l in open("1.in")]

print(X)
Q = []
for elf in ("\n".join(X)).split("\n\n"):
    print("elf", elf)
    q = 0
    for x in elf.split("\n"):
        q += int(x)
    Q.append(q)
print(max(Q))
print(Q.index(max(Q)) + 1)
