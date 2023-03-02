from collections import deque

# lines = open("example.in").read().strip().split("\n")
lines = open("21.in").read().strip().split("\n")

M = {}
for line in lines:
    m, n = line.split(": ")
    M[m] = n


def f(k, p, h_value=0):
    if p == 2 and k == "humn":
        return h_value
    try:
        return int(M[k])
    except:
        assert len(M[k].split()) == 3, M[k]
        x1, o, x2 = M[k].split()
        if o == "+":
            return f(x1, p, h_value) + f(x2, p, h_value)
        if o == "-":
            return f(x1, p, h_value) - f(x2, p, h_value)
        if o == "*":
            return f(x1, p, h_value) * f(x2, p, h_value)
        if o == "/":
            return f(x1, p, h_value) // f(x2, p, h_value)


# print(f("root", 1))
# which one has humn?
v1, v2 = [v.strip() for v in M["root"].split("+")]
print(v1, v2)
if f(v2, 2, 0) != f(v2, 2, 1):
    v1, v2 = v2, v1

print(v1, v2)
print(f(v2, 2))
# print(f(v1, 2, 301))
matching_value = f(v2, 2)

low = -1e20
high = 1e20
while True:
    mid = int((low + high) / 2)
    # print(mid)
    if f(v1, 2, mid) < matching_value:
        high = mid
    elif f(v1, 2, mid) > matching_value:
        low = mid
    else:
        print(mid)
        break

# Where to put high=mid / low=mid depends on equations involving humn.
