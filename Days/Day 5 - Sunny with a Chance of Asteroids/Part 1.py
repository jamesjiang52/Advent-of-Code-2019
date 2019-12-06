def main():
    f = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    input = 1
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
            f[f[i + 1]] = input
            i += 2
        elif opcode == 4:
            if immediate_1:
                print(f[i + 1])
            else:
                print(f[f[i + 1]])
            i += 2
        else:
            print("Something went wrong")
            break


if __name__ == "__main__":
    main()
