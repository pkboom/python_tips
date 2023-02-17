from collections import deque

lines = open("example.in").read().strip().split("\n")
lines = open("20.in").read().strip().split("\n")

X = [int(line) for line in lines]
Y = [int(line) for line in lines]
for x in X:
    while True:
        if Y[0] == x:
            break
        Y.append(Y.pop(0))
    y = Y.pop(Y.index(x))
    new_key = y % len(Y)
    for j in range(new_key):
        Y.append(Y.pop(0))
    Y.append(y)

# print(Y)
index = Y.index(0)
print(Y[(index + 1000) % len(Y)])
print(Y[(index + 2000) % len(Y)])
print(Y[(index + 3000) % len(Y)])
print(
    (Y[(index + 1000) % len(Y)])
    + (Y[(index + 2000) % len(Y)])
    + (Y[(index + 3000) % len(Y)])
)
