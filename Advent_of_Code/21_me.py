from collections import deque

# lines = open("example.in").read().strip().split("\n")
lines = open("21.in").read().strip().split("\n")

M1 = {}
M2 = {}
for line in lines:
    m, n = line.split(": ")
    if n.isnumeric():
        M1[m] = int(n)
    else:
        M2[m] = n

X = deque()
O = deque()
while M2:
    for k, v in M2.items():
        m1, o, m2 = v.split(" ")
        M1["humn"] = "x"
        if m1 in M1 and m2 in M1:
            if isinstance(M1[m1], int) and isinstance(M1[m2], int):
                M1[k] = int(eval(str(M1[m1]) + o + str(M1[m2])))
                # print(M1[k])
            else:
                for i in [M1[m1], M1[m2]]:
                    if isinstance(i, int):
                        X.append(i)
                        O.append(o)
                M1[k] = "(" + str(M1[m1]) + o + str(M1[m2]) + ")"
            M2.pop(k, None)
            break


def get_operation(o):
    match o:
        case "+":
            return "-"
        case "-":
            return "+"
        case "*":
            return "//"
        case "/":
            return "*"


ans = X.pop()
O.pop()
while O:
    # print(str(ans) + get_operation(O[-1]) + str(X[-1]))
    ans = eval(str(ans) + get_operation(O.pop()) + str(X.pop()))
print(ans)
# 9535830990200
# 113627984505092 55897899750372
# print(M1["root"])
