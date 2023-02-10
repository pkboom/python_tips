D = open("17.in").read().strip()


def get_piece(t, y):
    match t % 5:
        case 0:
            return set([(2, y), (3, y), (4, y), (5, y)])
        case 1:
            return set([(3, y), (2, y + 1), (3, y + 1), (4, y + 1), (3, y + 2)])
        case 2:
            return set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)])
        case 3:
            return set([(2, y), (2, y + 1), (2, y + 2), (2, y + 3)])
        case 4:
            return set([(2, y), (3, y), (2, y + 1), (3, y + 1)])
        case _:
            assert False, "can't find a rock."


def move_left(rock):
    if any([x == 0 for x, _ in rock]):
        return rock
    if set([(x - 1, y) for x, y in rock]) & C:
        return rock
    return set([(x - 1, y) for x, y in rock])


def move_right(rock):
    if any([x == 6 for x, _ in rock]):
        return rock
    if set([(x + 1, y) for x, y in rock]) & C:
        return rock
    return set([(x + 1, y) for x, y in rock])


def move_down(rock):
    return set([(x, y - 1) for x, y in rock])


def move_up(rock):
    return set([(x, y + 1) for x, y in rock])


def draw(rock):
    chamber = C | rock
    for j in range(max([y for _, y in chamber]), -1, -1):
        r = ""
        for i in range(7):
            if (i, j) in chamber:
                r += "#"
            else:
                r += "."
        print(r)
    print("=====================================")


def signature(height):
    return frozenset([(x, height - y) for (x, y) in C if height - y <= 30])


C = set([(i, 0) for i in range(7)])
p2 = 1000000000000
height = 0
c = 0
direction = -1
cache = {}
added = 0

while c < p2:
    rock = get_piece(c, height + 4)
    while True:
        direction = (direction + 1) % len(D)
        if D[direction] == "<":
            rock = move_left(rock)
        else:
            rock = move_right(rock)
        # draw(rock)
        rock = move_down(rock)
        if rock & C:
            rock = move_up(rock)
            C |= rock
            height = max([y for _, y in C])
            key = (direction, c % 5, signature(height))
            if key in cache and c > 2022:
                oldc, oldh = cache[key]
                diffc = c - oldc
                diffh = height - oldh
                remaining_count = p2 - c
                cycle = remaining_count // diffc
                added += cycle * diffh
                c += diffc * cycle
            cache[key] = (c, height)
            break
    c += 1
    if c == 2022:
        print(height)

print(added + height)
