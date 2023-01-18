with open("6.in") as f:
    X = [l for l in f.read()]

start_of_packet = 0

for i in range(len(X) - 13):
    if start_of_packet == 0 and len(set(X[i : i + 4])) == 4:
        start_of_packet = i + 4
        continue

    if len(set(X[i : i + 14])) == 14:
        break

print(start_of_packet)
print(i + 14)
