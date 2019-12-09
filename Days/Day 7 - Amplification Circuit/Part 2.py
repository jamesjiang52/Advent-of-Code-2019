import itertools


f_orig = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
f_all = [f_orig[:] for i in range(5)]
max_output = 0


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


def amplifier_loop(phase_setting):
    global f_all, max_output
    prev_output = 0
    j = 0
    positions = [0, 0, 0, 0, 0]
    seen_phase_settings = [0, 0, 0, 0, 0]
    seen_prev_outputs = [0, 0, 0, 0, 0]
    while True:
        i = positions[j]
        f = f_all[j]
        while True:
            opcode = int(str(f[i])[-2:])
            try:
                immediate = int(str(f[i])[:-2])
            except ValueError:
                immediate = 0
            i1 = immediate % 10
            i2 = immediate//10 % 10
            if opcode == 99:
                return
            elif opcode == 1:
                set_f(f, get_f(f, i + 1, i1) + get_f(f, i + 2, i2), i + 3, 0)
                i += 4
            elif opcode == 2:
                set_f(f, get_f(f, i + 1, i1)*get_f(f, i + 2, i2), i + 3, 0)
                i += 4
            elif opcode == 3:
                if not seen_phase_settings[j]:
                    f[f[i + 1]] = phase_setting[j]
                    seen_phase_settings[j] = 1
                elif not seen_prev_outputs[j]:
                    f[f[i + 1]] = prev_output
                    seen_prev_outputs[j] = 1
                else:  # go to next amplifier
                    break
                i += 2
            elif opcode == 4:  # go to next amplifier
                prev_output = get_f(f, i + 1, i1)
                if j == 4:
                    max_output = max(max_output, prev_output)
                seen_prev_outputs[(j + 1) % 5] = 0
                positions[j] = i + 2
                break
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

        j = (j + 1) % 5


def main():
    global f_all
    phases = itertools.permutations([5, 6, 7, 8, 9])
    for phase_setting in phases:
        amplifier_loop(phase_setting)
        f_all = [f_orig[:] for i in range(5)]
    print(max_output)


if __name__ == "__main__":
    main()
