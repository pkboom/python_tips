from collections import deque

# lines = open("example.in").read().strip().split("\n")
lines = open("20.in").read().strip().split("\n")


def solve(p):
    if p == 2:
        X = [int(line) * 811589153 for line in lines]
    else:
        X = [int(line) for line in lines]
    X = deque(list(enumerate(X)))
    for mixing in range(10 if p == 2 else 1):
        for i in range(len(X)):
            for j in range(len(X)):
                if X[j][0] == i:
                    break
            for _ in range(j):
                X.append(X.popleft())
            x = X.popleft()
            val = x[1]
            val = val % len(X)
            for _ in range(val):
                X.append(X.popleft())
            X.append(x)

    for i, x in enumerate(X):
        if x[1] == 0:
            break
    print(
        (X[(i + 1000) % len(X)][1])
        + (X[(i + 2000) % len(X)][1])
        + (X[(i + 3000) % len(X)][1])
    )


solve(1)
solve(2)
