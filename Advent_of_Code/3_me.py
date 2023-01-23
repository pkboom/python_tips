X = [l.strip() for l in open("3.in")]

lower = [chr(ord("a") + i) for i in range(26)]
upper = [chr(ord("A") + i) for i in range(26)]
alphabet = lower + upper

total = 0

for x in X:
    first_half, seond_half = x[: len(x) // 2], x[len(x) // 2 :]

    for ch1 in first_half:
        if ch1 in seond_half:
            print(ch1)
            print(alphabet.index(ch1) + 1)
            total += alphabet.index(ch1) + 1
            break

print(total)
