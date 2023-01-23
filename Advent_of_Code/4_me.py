X = [l.strip() for l in open("4.in")]

pairs_overlapped = 0
pairs_contained = 0

for i in X:
    a, b = i.split(",")

    a1, a2 = a.split("-")
    b1, b2 = b.split("-")

    a_list = list(range(int(a1), int(a2) + 1))
    b_list = list(range(int(b1), int(b2) + 1))

    if any(elem in a_list for elem in b_list) or any(elem in b_list for elem in a_list):
        pairs_overlapped += 1

    if all(elem in a_list for elem in b_list) or all(elem in b_list for elem in a_list):
        pairs_contained += 1
    # if set(a_list).issubset(b_list) or set(b_list).issubset(a_list):
    #     pairs_contained += 1

print(pairs_overlapped)
print(pairs_contained)
