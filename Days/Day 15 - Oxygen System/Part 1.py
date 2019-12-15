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


def visit(f, i, rel_base, direction):
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
            set_f(f, direction, i + 1, i1, rel_base)
            i += 2
        elif opcode == 4:
            out = get_f(f, i + 1, i1, rel_base)
            return out, i + 2, rel_base
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


def bfs(grid):
    queue = [((0, 0), 0)]
    seen = set()
    while queue:
        current_position, steps = queue.pop(0)
        seen.add(current_position)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (current_position[0] + dx, current_position[1] + dy) in seen:
                continue
            if (current_position[0] + dx, current_position[1] + dy) in grid and \
                    grid[(current_position[0] + dx, current_position[1] + dy)] in [1, 2]:
                if grid[(current_position[0] + dx, current_position[1] + dy)] == 2:
                    return steps + 1
                else:
                    queue.append(((current_position[0] + dx, current_position[1] + dy), steps + 1))


def main():
    f = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    f = dict(enumerate(f))
    i = 0
    rel_base = 0
    grid = {}
    current_position = (0, 0)
    queue = {}
    directions_stack = []
    oxygen_location = None
    while True:
        if current_position not in queue:
            queue[current_position] = [1, 2, 3, 4]
        if queue[current_position]:
            backtrack = False
            direction = queue[current_position].pop()
        else:
            backtrack = True
            if not directions_stack:
                break

            direction = directions_stack.pop()
            direction = {1: 2, 2: 1, 3: 4, 4: 3}[direction]

        out, i, rel_base = visit(f, i, rel_base, direction)
        if out in [1, 2]:
            if direction == 1:
                current_position = (current_position[0], current_position[1] + 1)
            elif direction == 2:
                current_position = (current_position[0], current_position[1] - 1)
            if direction == 3:
                current_position = (current_position[0] - 1, current_position[1])
            if direction == 4:
                current_position = (current_position[0] + 1, current_position[1])
            grid[current_position] = out

            if out == 2:
                oxygen_location = current_position

            if not backtrack:
                directions_stack.append(direction)

    assert oxygen_location
    print(bfs(grid))

if __name__ == "__main__":
    main()
