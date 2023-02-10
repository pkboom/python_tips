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


C = set([(i, 0) for i in range(7)])
p1 = 2022
p2 = 1000000000000
height = 0
count = 0
direction = -1

while True:
    rock = get_piece(count, height + 4)
    if count == 2022:
        print(height)
        break
    while True:
        # draw(rock)
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
            count += 1
            height = max([y for _, y in C])
            break
