def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    path_0 = f[0].split(",")
    path_1 = f[1].split(",")

    seen = set()
    curr_x, curr_y = (0, 0)
    for i in path_0:
        direction = i[0]
        if direction == "R":
            dx, dy = (1, 0)
        elif direction == "D":
            dx, dy = (0, -1)
        elif direction == "L":
            dx, dy = (-1, 0)
        else:
            dx, dy = (0, 1)

        for j in range(1, int(i[1:]) + 1):
            seen.add((curr_x + j*dx, curr_y + j*dy))

        curr_x += int(i[1:])*dx
        curr_y += int(i[1:])*dy

    curr_x, curr_y = (0, 0)
    min_dist = 2**32
    for i in path_1:
        direction = i[0]
        if direction == "R":
            dx, dy = (1, 0)
        elif direction == "D":
            dx, dy = (0, -1)
        elif direction == "L":
            dx, dy = (-1, 0)
        else:
            dx, dy = (0, 1)

        for j in range(1, int(i[1:]) + 1):
            if (curr_x + j*dx, curr_y + j*dy) in seen:
                min_dist = min(min_dist, abs(curr_x + j*dx) + abs(curr_y + j*dy))

        curr_x += int(i[1:])*dx
        curr_y += int(i[1:])*dy

    print(min_dist)


if __name__ == "__main__":
    main()
