def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    orbits = [line.split(")") for line in f]
    orbits_dict = {}
    for orbit in orbits:
        orbits_dict[orbit[0]] = 0
        orbits_dict[orbit[1]] = 0
    for i in range(len(orbits)):
        for orbit in orbits:
            orbits_dict[orbit[1]] = orbits_dict[orbit[0]] + 1
    print(sum(orbits_dict.values()))


if __name__ == "__main__":
    main()
