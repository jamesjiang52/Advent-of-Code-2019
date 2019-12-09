def get_f(f, i, mode):
    try:
        if mode == 0:
            return f[f[i]]
        if mode == 1:
            return f[i]
    except KeyError:
        return 0
    raise NotImplementedError


def set_f(f, value, i, mode):
    if mode == 0:
        f[f[i]] = value
        return
    if mode == 1:
        f[i] = value
        return
    raise NotImplementedError


def main():
    f = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    input = 5
    i = 0
    while True:
        opcode = int(str(f[i])[-2:])
        try:
            immediate = int(str(f[i])[:-2])
        except ValueError:
            immediate = 0
        i1 = immediate % 10
        i2 = immediate//10 % 10
        if opcode == 99:
            break
        elif opcode == 1:
            set_f(f, get_f(f, i + 1, i1) + get_f(f, i + 2, i2), i + 3, 0)
            i += 4
        elif opcode == 2:
            set_f(f, get_f(f, i + 1, i1)*get_f(f, i + 2, i2), i + 3, 0)
            i += 4
        elif opcode == 3:
            set_f(f, input, i + 1, 0)
            i += 2
        elif opcode == 4:
            print(get_f(f, i + 1, i1))
            i += 2
        elif opcode == 5:
            if get_f(f, i + 1, i1):
                i = get_f(f, i + 2, i2)
            else:
                i += 3
        elif opcode == 6:
            if not get_f(f, i + 1, i1):
                i = get_f(f, i + 2, i2)
            else:
                i += 3
        elif opcode == 7:
            if get_f(f, i + 1, i1) < get_f(f, i + 2, i2):
                set_f(f, 1, i + 3, 0)
            else:
                set_f(f, 0, i + 3, 0)
            i += 4
        elif opcode == 8:
            if get_f(f, i + 1, i1) == get_f(f, i + 2, i2):
                set_f(f, 1, i + 3, 0)
            else:
                set_f(f, 0, i + 3, 0)
            i += 4
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
