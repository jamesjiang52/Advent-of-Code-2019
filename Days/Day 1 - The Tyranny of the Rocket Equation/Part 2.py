def fuel(x):
    if int(x) < 6:
        return 0
    y = int(x)//3 - 2
    return y + fuel(y)


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    print(sum(map(fuel, f)))


if __name__ == "__main__":
    main()

