def main():
    f = [*map(int, list([line.rstrip("\n") for line in open("Data.txt")][0]))]
    num_elements = len(f)
    for i in range(100):
        new_f = []
        sums = [f[0]]
        for j in range(1, num_elements):
            sums.append(sums[j - 1] + f[j])
        for j in range(num_elements):
            total = 0
            step = j + 1
            phase = 1
            for k in range(j, num_elements, step*2):
                try:
                    if k == 0:
                        total += sums[k + j]*phase
                    else:
                        total += (sums[k + j] - sums[k - 1])*phase
                except IndexError:
                    total += (sums[-1] - sums[k - 1])*phase
                phase *= -1
            new_f.append(abs(total) % 10)
        f = new_f

    print("".join([str(i) for i in f[0:8]]))


if __name__ == "__main__":
    main()
