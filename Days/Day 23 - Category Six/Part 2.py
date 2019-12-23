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
    f_orig = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    f_orig = dict(enumerate(f_orig))
    f_all = [f_orig.copy() for i in range(50)]
    i_all = [0]*50
    rel_base_all = [0]*50
    address = 0
    current = 0
    initialized = False
    queue_all = [[] for i in range(50)]
    queue_processing_bool_all = [False]*50
    queue_processing_all = [(0, 0)]*50
    out_processing_bool_all = [False]*50
    out_processing_all = [(-1, 0, 0)]*50
    nat = (None, None)
    prev_y = -1
    while True:
        if current == 0:
            idle = True
        f = f_all[current]
        queue = queue_all[current]
        while True:
            i = i_all[current]
            rel_base = rel_base_all[current]
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
                i_all[current] += 4
            elif opcode == 2:
                set_f(f, get_f(f, i + 1, i1, rel_base)*get_f(f, i + 2, i2, rel_base), i + 3, i3, rel_base)
                i_all[current] += 4
            elif opcode == 3:
                if not initialized:
                    input = address
                    address += 1
                elif queue_processing_bool_all[current]:
                    input = queue_processing_all[current][1]
                    queue_processing_bool_all[current] = False
                elif queue:
                    idle = False
                    x, y = queue.pop(0)
                    queue_processing_all[current] = (x, y)
                    input = x
                    queue_processing_bool_all[current] = True
                    set_f(f, input, i + 1, i1, rel_base)
                    i_all[current] += 2
                    continue
                else:
                    input = -1
                set_f(f, input, i + 1, i1, rel_base)
                i_all[current] += 2
                break
            elif opcode == 4:
                out = get_f(f, i + 1, i1, rel_base)
                if out_processing_all[current][0] == -1:
                    out_processing_all[current] = (out, 0, 0)
                elif out_processing_bool_all[current]:
                    out_processing_all[current] = (out_processing_all[current][0], out_processing_all[current][1], out)
                    if out_processing_all[current][0] == 255:
                        nat = (out_processing_all[current][1], out_processing_all[current][2])
                    else:
                        queue_all[out_processing_all[current][0]].append((out_processing_all[current][1], out_processing_all[current][2]))
                    out_processing_all[current] = (-1, 0, 0)
                    out_processing_bool_all[current] = False
                else:
                    out_processing_all[current] = (out_processing_all[current][0], out, 0)
                    out_processing_bool_all[current] = True
                i_all[current] += 2
            elif opcode == 5:
                if get_f(f, i + 1, i1, rel_base):
                    i_all[current] = get_f(f, i + 2, i2, rel_base)
                else:
                    i_all[current] += 3
            elif opcode == 6:
                if not get_f(f, i + 1, i1, rel_base):
                    i_all[current] = get_f(f, i + 2, i2, rel_base)
                else:
                    i_all[current] += 3
            elif opcode == 7:
                if get_f(f, i + 1, i1, rel_base) < get_f(f, i + 2, i2, rel_base):
                    set_f(f, 1, i + 3, i3, rel_base)
                else:
                    set_f(f, 0, i + 3, i3, rel_base)
                i_all[current] += 4
            elif opcode == 8:
                if get_f(f, i + 1, i1, rel_base) == get_f(f, i + 2, i2, rel_base):
                    set_f(f, 1, i + 3, i3, rel_base)
                else:
                    set_f(f, 0, i + 3, i3, rel_base)
                i_all[current] += 4
            elif opcode == 9:
                rel_base_all[current] += get_f(f, i + 1, i1, rel_base)
                i_all[current] += 2
            else:
                raise NotImplementedError
        if current == 49:
            if not initialized:
                initialized = True
            if idle:
                if nat != (None, None):
                    queue_all[0].append(nat)
                    if nat[1] == prev_y:
                        print(prev_y)
                        break
                    prev_y = nat[1]
                    nat = (None, None)
        current = (current + 1) % 50


if __name__ == "__main__":
    main()
