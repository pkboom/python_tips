with open("8.in") as f:
    lines = [l.strip() for l in f]

visible = []
scenic = []


def in_forest(lines, xp, yp, direction, count):
    if direction == "left":
        position = yp - 1 * count
        return position, position >= 0
    elif direction == "right":
        position = yp + 1 * count
        return (
            position,
            position < len(lines[0]),
        )
    elif direction == "up":
        position = xp - 1 * count
        return position, position >= 0
    else:
        position = xp + 1 * count
        return (
            position,
            position < len(lines),
        )


def get_value(lines, xp, yp, direction, position):
    if direction == "left":
        return lines[xp][position]
    elif direction == "right":
        return lines[xp][position]
    elif direction == "up":
        return lines[position][yp]
    else:
        return lines[position][yp]


def is_blocking(lines, yv, yp, xv, xp):
    for direction in ["left", "right", "up", "down"]:
        c = 1

        while True:
            position, inside_forest = in_forest(lines, xp, yp, direction, c)

            if not inside_forest:
                return False

            value = get_value(lines, xp, yp, direction, position)

            if value >= yv:
                break

            c += 1

    return True


def get_scenic_score(lines, yv, yp, xv, xp):
    score = 1

    for direction in ["left", "right", "up", "down"]:
        c = 1

        while True:
            position, inside_forest = in_forest(lines, xp, yp, direction, c)

            if not inside_forest:
                print("inside_forest c", c)
                score *= c - 1
                break

            value = get_value(lines, xp, yp, direction, position)

            if value >= yv:
                print("value >= yv c", c)
                score *= c
                break

            c += 1

    return score


for xp in range(len(lines)):
    xv = lines[xp]

    for yp in range(len(xv)):
        yv = xv[yp]

        if not is_blocking(lines, yv, yp, xv, xp):
            visible.append((xp, yp))

        scenic.append(get_scenic_score(lines, yv, yp, xv, xp))

print(len(set(visible)))
print(scenic)
print(max(scenic))
