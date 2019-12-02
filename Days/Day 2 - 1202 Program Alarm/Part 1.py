def main():
    f = [int(i) for i in [line.rstrip("\n") for line in open("Data.txt")][0].split(",")]
    f[1] = 12
    f[2] = 2
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
    print(f[0])


if __name__ == "__main__":
    main()
