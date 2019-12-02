def main():
    f_orig = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    for noun in range(100):
        for verb in range(100):
            f = f_orig[:]
            f[1] = noun
            f[2] = verb
            i = 0
            while True:
                if f[i] == 99:
                    break
                elif f[i] == 1:
                    f[f[i + 3]] = f[f[i + 1]] + f[f[i + 2]]
                elif f[i] == 2:
                    f[f[i + 3]] = f[f[i + 1]]*f[f[i + 2]]
                else:
                    print("Something went wrong")
                i += 4

            if f[0] == 19690720:
                print(100*noun + verb)
                return


if __name__ == "__main__":
    main()
