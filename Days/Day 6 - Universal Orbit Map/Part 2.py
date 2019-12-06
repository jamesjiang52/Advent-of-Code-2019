def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    orbits = [line.split(")") for line in f]
    orbits_dict = {}
    orbits_next_hop = {}
    for orbit in orbits:
        orbits_dict[orbit[0]] = 0
        orbits_dict[orbit[1]] = 0
        orbits_next_hop[orbit[0]] = None
        orbits_next_hop[orbit[1]] = None
    for i in range(len(orbits)):
        for orbit in orbits:
            orbits_dict[orbit[1]] = orbits_dict[orbit[0]] + 1
            if i == 0:
                orbits_next_hop[orbit[1]] = orbit[0]

    seen = {}
    count = 0
    current = "YOU"
    while current != "COM":
        seen[orbits_next_hop[current]] = count
        current = orbits_next_hop[current]
        count += 1
    count = 0
    current = "SAN"
    while current != "COM":
        if orbits_next_hop[current] in seen:
            print(count + seen[orbits_next_hop[current]])
            break
        current = orbits_next_hop[current]
        count += 1


if __name__ == "__main__":
    main()
