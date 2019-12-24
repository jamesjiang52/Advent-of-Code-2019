def evolve(f):
    new_f = [""]*len(f)
    for i in range(len(f)):
        for j in range(len(f[0])):
            count_adjacent = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + dy < len(f) and 0 <= j + dx < len(f[0]):
                    if f[i + dy][j + dx] == "#":
                        count_adjacent += 1
            if f[i][j] == "#" and count_adjacent != 1:
                new_f[i] += "."
            elif f[i][j] == "." and count_adjacent in [1, 2]:
                new_f[i] += "#"
            else:
                new_f[i] += f[i][j]
    return new_f


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    seen = set()
    seen.add("".join(f))
    while True:
        f = evolve(f)
        if "".join(f) in seen:
            biodiversity = 0
            for i in range(len(f)):
                for j in range(len(f[0])):
                    if f[i][j] == "#":
                        biodiversity += 2**(i*5 + j)
            print(biodiversity)
            break
        seen.add("".join(f))


if __name__ == "__main__":
    main()
