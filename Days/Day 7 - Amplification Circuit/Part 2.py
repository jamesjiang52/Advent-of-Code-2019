import itertools


f_orig = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
f_all = [f_orig[:] for i in range(5)]
max_output = 0


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
            immediate_1 = immediate % 10
            immediate_2 = immediate//10 % 10
            if opcode == 99:
                return
            elif opcode == 1:
                if immediate_1 and immediate_2:
                    f[f[i + 3]] = f[i + 1] + f[i + 2]
                elif immediate_1 and not immediate_2:
                    f[f[i + 3]] = f[i + 1] + f[f[i + 2]]
                elif not immediate_1 and immediate_2:
                    f[f[i + 3]] = f[f[i + 1]] + f[i + 2]
                else:
                    f[f[i + 3]] = f[f[i + 1]] + f[f[i + 2]]
                i += 4
            elif opcode == 2:
                if immediate_1 and immediate_2:
                    f[f[i + 3]] = f[i + 1]*f[i + 2]
                elif immediate_1 and not immediate_2:
                    f[f[i + 3]] = f[i + 1]*f[f[i + 2]]
                elif not immediate_1 and immediate_2:
                    f[f[i + 3]] = f[f[i + 1]]*f[i + 2]
                else:
                    f[f[i + 3]] = f[f[i + 1]]*f[f[i + 2]]
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
                if immediate_1:
                    prev_output = f[i + 1]
                    if j == 4:
                        max_output = max(max_output, f[i + 1])
                else:
                    prev_output = f[f[i + 1]]
                    if j == 4:
                        max_output = max(max_output, f[f[i + 1]])
                seen_prev_outputs[(j + 1) % 5] = 0
                positions[j] = i + 2
                break
            elif opcode == 5:
                if immediate_1 and immediate_2:
                    if f[i + 1]:
                        i = f[i + 2]
                    else:
                        i += 3
                elif immediate_1 and not immediate_2:
                    if f[i + 1]:
                        i = f[f[i + 2]]
                    else:
                        i += 3
                elif not immediate_1 and immediate_2:
                    if f[f[i + 1]]:
                        i = f[i + 2]
                    else:
                        i += 3
                elif not immediate_1 and not immediate_2:
                    if f[f[i + 1]]:
                        i = f[f[i + 2]]
                    else:
                        i += 3
            elif opcode == 6:
                if immediate_1 and immediate_2:
                    if not f[i + 1]:
                        i = f[i + 2]
                    else:
                        i += 3
                elif immediate_1 and not immediate_2:
                    if not f[i + 1]:
                        i = f[f[i + 2]]
                    else:
                        i += 3
                elif not immediate_1 and immediate_2:
                    if not f[f[i + 1]]:
                        i = f[i + 2]
                    else:
                        i += 3
                elif not immediate_1 and not immediate_2:
                    if not f[f[i + 1]]:
                        i = f[f[i + 2]]
                    else:
                        i += 3
            elif opcode == 7:
                if immediate_1 and immediate_2:
                    if f[i + 1] < f[i + 2]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                elif immediate_1 and not immediate_2:
                    if f[i + 1] < f[f[i + 2]]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                elif not immediate_1 and immediate_2:
                    if f[f[i + 1]] < f[i + 2]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                elif not immediate_1 and not immediate_2:
                    if f[f[i + 1]] < f[f[i + 2]]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                i += 4
            elif opcode == 8:
                if immediate_1 and immediate_2:
                    if f[i + 1] == f[i + 2]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                elif immediate_1 and not immediate_2:
                    if f[i + 1] == f[f[i + 2]]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                elif not immediate_1 and immediate_2:
                    if f[f[i + 1]] == f[i + 2]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                elif not immediate_1 and not immediate_2:
                    if f[f[i + 1]] == f[f[i + 2]]:
                        f[f[i + 3]] = 1
                    else:
                        f[f[i + 3]] = 0
                i += 4
            else:
                print("Something went wrong")
                break

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
