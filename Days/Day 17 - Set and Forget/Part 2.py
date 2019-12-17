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
    f[0] = 2
    i = 0
    rel_base = 0

    # found these manually...
    A = ["L", ",", "8", ",", "R", ",", "1", "0", ",", "L", ",", "1", "0"]
    B = ["R", ",", "1", "0", ",", "L", ",", "8", ",", "L", ",", "8", ",", "L", ",", "1", "0"]
    C = ["L", ",", "4", ",", "L", ",", "6", ",", "L", ",", "8", ",", "L", ",", "8"]
    rules = [
        ["A", ",", "B", ",", "A", ",", "C", ",", "B",",", "C", ",", "A", ",", "C", ",", "B", ",", "C"],
        A, B, C
    ]
    ascii_rules = [[ord(i) for i in row] + [10] for row in rules]
    ascii_rules_flat = [i for row in ascii_rules for i in row] + [ord("n"), 10]

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
            input = ascii_rules_flat.pop(0)
            set_f(f, input, i + 1, i1, rel_base)
            i += 2
        elif opcode == 4:
            char_code = get_f(f, i + 1, i1, rel_base)
            if char_code > 255:
                print(char_code)
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


if __name__ == "__main__":
    main()