def main():
    positions = [
        [10, 15, 7],
        [15, 10, 0],
        [20, 12, 3],
        [0, -3, 13]
    ]
    velocities = [[0]*3 for i in range(4)]

    for i in range(1000):
        for j in range(0, 3):
            for k in range(j, 4):
                for axis in range(3):
                    if positions[j][axis] > positions[k][axis]:
                        velocities[j][axis] += -1
                        velocities[k][axis] += 1
                    elif positions[j][axis] < positions[k][axis]:
                        velocities[j][axis] += 1
                        velocities[k][axis] += -1
        for j in range(4):
            for axis in range(3):
                positions[j][axis] += velocities[j][axis]

    print(sum([sum(map(abs, positions[i]))*sum(map(abs, velocities[i])) for i in range(4)]))


if __name__ == "__main__":
    main()
