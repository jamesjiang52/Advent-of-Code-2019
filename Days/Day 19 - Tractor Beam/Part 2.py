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


def in_beam(f, x, y):
    i = 0
    rel_base = 0
    x_given = False
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
            if not x_given:
                input = x
                x_given = True
            else:
                input = y
            set_f(f, input, i + 1, i1, rel_base)
            i += 2
        elif opcode == 4:
            return get_f(f, i + 1, i1, rel_base)
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


def main():
    f_orig = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    f_orig = dict(enumerate(f_orig))
    count = 0
    x = 99
    y = 110
    while True:
        if in_beam(f_orig.copy(), x, y):
            if in_beam(f_orig.copy(), x + 1, y):
                x += 1
            else:
                if in_beam(f_orig.copy(), x - 99, y) and in_beam(f_orig.copy(), x - 99, y + 99):
                    print(10000*(x - 99) + y)
                    break
                else:
                    y += 1
        else:
            print("Something went wrong at ", x, y)
            break


if __name__ == "__main__":
    main()
