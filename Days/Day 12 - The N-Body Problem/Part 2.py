import math
from copy import deepcopy


def lcm(x, y):
    return abs(x*y)//math.gcd(x, y)


def main():
    positions = [
        [10, 15, 7],
        [15, 10, 0],
        [20, 12, 3],
        [0, -3, 13]
    ]
    velocities = [[0]*3 for i in range(4)]

    positions_t = [
        [10, 15, 20, 0],
        [15, 10, 12, -3],
        [7, 0, 3, 13]
    ]
    velocities_t = [[0]*4 for i in range(3)]

    initial_positions_t = deepcopy(positions_t)
    initial_velocities_t = deepcopy(velocities_t)
    periods = [0, 0, 0]

    for axis in range(3):
        i = 0
        seen = set()
        while True:
            for j in range(0, 3):
                for k in range(j, 4):
                    if positions_t[axis][j] > positions_t[axis][k]:
                        velocities_t[axis][j] += -1
                        velocities_t[axis][k] += 1
                    elif positions_t[axis][j] < positions_t[axis][k]:
                        velocities_t[axis][j] += 1
                        velocities_t[axis][k] += -1
            for j in range(4):
                positions_t[axis][j] += velocities_t[axis][j]
            if str([positions_t[axis], velocities_t[axis]]) in seen:
                periods[axis] = i
                break

            seen.add(str([positions_t[axis], velocities_t[axis]]))
            i += 1

    print(lcm(lcm(periods[0], periods[1]), periods[2]))


if __name__ == "__main__":
    main()
