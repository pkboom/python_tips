with open("8.in") as f:
    lines = [l.strip() for l in f]

visible = []


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


for xp in range(len(lines)):
    xv = lines[xp]

    for yp in range(len(xv)):
        yv = xv[yp]

        if not is_blocking(lines, yv, yp, xv, xp):
            visible.append((xp, yp))

print(len(set(visible)))
