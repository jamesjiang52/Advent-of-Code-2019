def main():
    f = [*map(int, list([line.rstrip("\n") for line in open("Data.txt")][0]))]*10000
    offset = int("".join([str(i) for i in f[0:7]]))
    f = f[offset:]
    num_elements = len(f)
    for i in range(100):
        new_f = []
        sum_ = sum(f)
        for j in range(num_elements):
            new_f.append(sum_ % 10)
            sum_ -= f[j]
        f = new_f

    print("".join([str(i) for i in f[0:8]]))


if __name__ == "__main__":
    main()
