def fuel(x):
    return int(x)//3 - 2


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    print(sum(map(fuel, f)))


if __name__ == "__main__":
    main()
