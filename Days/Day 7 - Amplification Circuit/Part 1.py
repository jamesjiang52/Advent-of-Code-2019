import itertools


def main():
    f = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    f_orig = f[:]
    phases = itertools.permutations([0, 1, 2, 3, 4])
    seen_phase_setting = 0
    max_output = 0
    for phase_setting in phases:
        prev_output = 0
        for j in range(5):
            i = 0
            while True:
                opcode = int(str(f[i])[-2:])
                try:
                    immediate = int(str(f[i])[:-2])
                except ValueError:
                    immediate = 0
                immediate_1 = immediate % 10
                immediate_2 = immediate//10 % 10
                if opcode == 99:
                    break
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
                    if not seen_phase_setting:
                        f[f[i + 1]] = phase_setting[j]
                        seen_phase_setting = 1
                    else:
                        f[f[i + 1]] = prev_output
                    i += 2
                elif opcode == 4:
                    if immediate_1:
                        prev_output = f[i + 1]
                        if j == 4:
                            max_output = max(max_output, f[i + 1])
                    else:
                        prev_output = f[f[i + 1]]
                        if j == 4:
                            max_output = max(max_output, f[f[i + 1]])
                    i += 2
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

            f = f_orig[:]
            seen_phase_setting = 0

    print(max_output)


if __name__ == "__main__":
    main()
