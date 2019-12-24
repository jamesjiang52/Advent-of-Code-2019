def evolve(f_dict):
    new_f_dict = {}
    min_level = min(f_dict.keys())
    if f_dict[min_level] != ["....." for i in range(5)]:
        f_dict[min_level - 1] = ["....." for i in range(5)]
    max_level = max(f_dict.keys())
    if f_dict[max_level] != ["....." for i in range(5)]:
        f_dict[max_level + 1] = ["....." for i in range(5)]
    for k, f in f_dict.items():
        new_f = [""]*5
        for i in range(5):
            for j in range(5):
                count_adjacent = 0
                if (j, i) in [(1, 1), (3, 1), (1, 3), (3, 3)]:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                elif (j, i) in [(1, 0), (2, 0), (3, 0)]:
                    for dx, dy in [(-1, 0), (1, 0), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict and f_dict[k - 1][1][2] == "#":
                        count_adjacent += 1
                elif (j, i) in [(1, 4), (2, 4), (3, 4)]:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict and f_dict[k - 1][3][2] == "#":
                        count_adjacent += 1
                elif (j, i) in [(0, 1), (0, 2), (0, 3)]:
                    for dx, dy in [(1, 0), (0, -1), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict and f_dict[k - 1][2][1] == "#":
                        count_adjacent += 1
                elif (j, i) in [(4, 1), (4, 2), (4, 3)]:
                    for dx, dy in [(-1, 0), (0, -1), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict and f_dict[k - 1][2][3] == "#":
                        count_adjacent += 1
                elif (j, i) == (0, 0):
                    for dx, dy in [(1, 0), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict:
                        for (x, y) in [(2, 1), (1, 2)]:
                            if f_dict[k - 1][y][x] == "#":
                                count_adjacent += 1
                elif (j, i) == (4, 0):
                    for dx, dy in [(-1, 0), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict:
                        for (x, y) in [(2, 1), (3, 2)]:
                            if f_dict[k - 1][y][x] == "#":
                                count_adjacent += 1
                elif (j, i) == (0, 4):
                    for dx, dy in [(1, 0), (0, -1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict:
                        for (x, y) in [(2, 3), (1, 2)]:
                            if f_dict[k - 1][y][x] == "#":
                                count_adjacent += 1
                elif (j, i) == (4, 4):
                    for dx, dy in [(-1, 0), (0, -1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k - 1 in f_dict:
                        for (x, y) in [(2, 3), (3, 2)]:
                            if f_dict[k - 1][y][x] == "#":
                                count_adjacent += 1
                elif (j, i) == (2, 1):
                    for dx, dy in [(-1, 0), (1, 0), (0, -1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k + 1 in f_dict:
                        for x in range(5):
                            if f_dict[k + 1][0][x] == "#":
                                count_adjacent += 1
                elif (j, i) == (1, 2):
                    for dx, dy in [(-1, 0), (0, -1), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k + 1 in f_dict:
                        for y in range(5):
                            if f_dict[k + 1][y][0] == "#":
                                count_adjacent += 1
                elif (j, i) == (2, 3):
                    for dx, dy in [(-1, 0), (1, 0), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k + 1 in f_dict:
                        for x in range(5):
                            if f_dict[k + 1][4][x] == "#":
                                count_adjacent += 1
                elif (j, i) == (3, 2):
                    for dx, dy in [(1, 0), (0, -1), (0, 1)]:
                        if f[i + dy][j + dx] == "#":
                            count_adjacent += 1
                    if k + 1 in f_dict:
                        for y in range(5):
                            if f_dict[k + 1][y][4] == "#":
                                count_adjacent += 1
                if f[i][j] == "#" and count_adjacent != 1:
                    new_f[i] += "."
                elif f[i][j] == "." and count_adjacent in [1, 2]:
                    new_f[i] += "#"
                else:
                    new_f[i] += f[i][j]
        new_f_dict[k] = new_f
    return new_f_dict


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    f_dict = {}
    f_dict[0] = f
    for k in range(200):
        f_dict = evolve(f_dict)
    count_bugs = 0
    for f in f_dict.values():
        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[i][j] == "#":
                    count_bugs += 1
    print(count_bugs)


if __name__ == "__main__":
    main()
