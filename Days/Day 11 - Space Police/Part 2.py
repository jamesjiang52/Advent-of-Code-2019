def get_f(f, i, mode, rel_base):
    try:
        if mode == 0:
            return f[f[i]]
        if mode == 1:
            return f[i]
        if mode == 2:
            return f[f[i] + rel_base]
    except KeyError:
        return 0
    raise NotImplementedError


def set_f(f, value, i, mode, rel_base):
    if mode == 0:
        f[f[i]] = value
        return
    if mode == 1:
        f[i] = value
        return
    if mode == 2:
        f[f[i] + rel_base] = value
        return
    raise NotImplementedError


def main():
    f = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    f = dict(enumerate(f))
    grid = {(0, 0): 1}
    current_pos = (0, 0)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir_index = 0
    i = 0
    rel_base = 0
    painted = False
    while True:
        opcode = int(str(f[i])[-2:])
        try:
            immediate = int(str(f[i])[:-2])
        except ValueError:
            immediate = 0
        i1 = immediate % 10
        i2 = immediate//10 % 10
        i3 = immediate//100 % 10
        if opcode == 99:
            break
        elif opcode == 1:
            set_f(f, get_f(f, i + 1, i1, rel_base) + get_f(f, i + 2, i2, rel_base), i + 3, i3, rel_base)
            i += 4
        elif opcode == 2:
            set_f(f, get_f(f, i + 1, i1, rel_base)*get_f(f, i + 2, i2, rel_base), i + 3, i3, rel_base)
            i += 4
        elif opcode == 3:
            if current_pos in grid:
                input = grid[current_pos]
            else:
                input = 0
            set_f(f, input, i + 1, i1, rel_base)
            i += 2
        elif opcode == 4:
            if not painted:
                grid[current_pos] = get_f(f, i + 1, i1, rel_base)
                painted = True
            else:
                turn = get_f(f, i + 1, i1, rel_base)
                if turn == 0:
                    current_dir_index = (current_dir_index - 1) % len(dirs)
                else:
                    current_dir_index = (current_dir_index + 1) % len(dirs)
                current_pos = (
                    current_pos[0] + dirs[current_dir_index][0],
                    current_pos[1] + dirs[current_dir_index][1]
                )
                painted = False
            i += 2
        elif opcode == 5:
            if get_f(f, i + 1, i1, rel_base):
                i = get_f(f, i + 2, i2, rel_base)
            else:
                i += 3
        elif opcode == 6:
            if not get_f(f, i + 1, i1, rel_base):
                i = get_f(f, i + 2, i2, rel_base)
            else:
                i += 3
        elif opcode == 7:
            if get_f(f, i + 1, i1, rel_base) < get_f(f, i + 2, i2, rel_base):
                set_f(f, 1, i + 3, i3, rel_base)
            else:
                set_f(f, 0, i + 3, i3, rel_base)
            i += 4
        elif opcode == 8:
            if get_f(f, i + 1, i1, rel_base) == get_f(f, i + 2, i2, rel_base):
                set_f(f, 1, i + 3, i3, rel_base)
            else:
                set_f(f, 0, i + 3, i3, rel_base)
            i += 4
        elif opcode == 9:
            rel_base += get_f(f, i + 1, i1, rel_base)
            i += 2
        else:
            raise NotImplementedError

    x_bounds = [0, 0]
    y_bounds = [0, 0]
    for x, y in grid.keys():
        x_bounds[0] = min(x_bounds[0], x)
        x_bounds[1] = max(x_bounds[1], x)
        y_bounds[0] = min(y_bounds[0], y)
        y_bounds[1] = max(y_bounds[1], y)

    paint = [[0]*(x_bounds[1] - x_bounds[0] + 1) for i in range(y_bounds[1] - y_bounds[0] + 1)]
    for y in range(y_bounds[1] - y_bounds[0] + 1):
        for x in range(x_bounds[1] - x_bounds[0] + 1):
            if (x + x_bounds[0], y_bounds[1] - y) in grid:
                if grid[(x + x_bounds[0], y_bounds[1] - y)] == 1:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                print(".", end="")
        print("")

if __name__ == "__main__":
    main()
