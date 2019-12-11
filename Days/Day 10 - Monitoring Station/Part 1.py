def get_visible_asteroids(f, i, j):
    ratios = dict()
    asteroids = set()
    for m in range(len(f)):
        for n in range(len(f[0])):
            if f[m][n] == "#":
                if n != j:
                    if n > j and (((m - i)/(n - j), "r") not in ratios or \
                            abs(ratios[((m - i)/(n - j), "r")][0] - i) + abs(ratios[((m - i)/(n - j), "r")][1] - j) > abs(m - i) + abs(n - j)):
                        try:
                            asteroids.remove(ratios[((m - i)/(n - j), "r")])
                        except KeyError:
                            pass
                        asteroids.add((m, n))
                        ratios[((m - i)/(n - j), "r")] = (m, n)
                    elif n < j and (((m - i)/(n - j), "l") not in ratios or \
                            abs(ratios[((m - i)/(n - j), "l")][0] - i) + abs(ratios[((m - i)/(n - j), "l")][1] - j) > abs(m - i) + abs(n - j)):
                        try:
                            asteroids.remove(ratios[((m - i)/(n - j), "l")])
                        except KeyError:
                            pass
                        asteroids.add((m, n))
                        ratios[((m - i)/(n - j), "l")] = (m, n)
                else:
                    if m > i and (999 not in ratios or \
                            abs(ratios[999][0] - i) + abs(ratios[999][1] - j) > abs(m - i) + abs(n - j)):
                        try:
                            asteroids.remove(ratios[999])
                        except KeyError:
                            pass
                        asteroids.add((m, n))
                        ratios[999] = (m, n)
                    elif m < i and (-999 not in ratios or \
                            abs(ratios[-999][0] - i) + abs(ratios[-999][1] - j) > abs(m - i) + abs(n - j)):
                        try:
                            asteroids.remove(ratios[-999])
                        except KeyError:
                            pass
                        asteroids.add((m, n))
                        ratios[-999] = (m, n)
    return(asteroids)


def main():
    f = [list(line.rstrip("\n")) for line in open("Data.txt")]
    max_asteroids = 0
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == "#":
                max_asteroids = max(max_asteroids, len(get_visible_asteroids(f, i, j)))

    print(max_asteroids)


if __name__ == "__main__":
    main()
