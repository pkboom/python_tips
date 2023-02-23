from collections import deque

lines = open("example.in").read().split("\n\n")
# lines = open("22.in").read().split("\n")

map = [line for line in lines[:-1][0].split("\n")]
path = lines[-1]

print(map, path)

c = 0
direction = ""
move = ""
point = [0, 0]
while c < len(path):
    move += path[c]
    if path[c] == "R" or path[c] == "L":
        direction = move[-1]
        move = int(move[:-1])
        dc = 0
        while dc < move:
            if direction == "R":
                while True:
                    tile = map[point[0]][point[1]]
                    if tile != " ":
                        break
                    point[1] = (point[1] + 1) % len(map[0])
                print(point)
                if tile == ".":
                    point[1] += 1
                    dc += 1
                elif tile == "#":
                    point[1] -= 1
                    print(point)
                    break
            else:
                while True:
                    tile = map[point[0]][point[1]]
                    if tile != " ":
                        break
                    point[0] = (point[0] + 1) % len(map)
                if tile == ".":
                    point[0] += 1
                    dc += 1
                elif tile == "#":
                    point[0] -= 1
                    break
                print(point)

        print(move, direction)
        move = ""
        direction = ""
    c += 1
