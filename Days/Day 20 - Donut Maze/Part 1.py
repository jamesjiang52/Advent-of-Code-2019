from collections import deque


def get_other_portal(portals, current_position, portal_name):
    pair = portals[portal_name]
    if current_position == pair[0]:
        return pair[1]
    elif current_position == pair[1]:
        return pair[0]
    raise NotImplementedError


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    portals = {}
    portal_locations = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == ".":
                if f[i - 1][j] in alphabet:
                    if f[i - 2][j] + f[i - 1][j] in portals:
                        portals[f[i - 2][j] + f[i - 1][j]].append((j, i))
                    else:
                        portals[f[i - 2][j] + f[i - 1][j]] = [(j, i)]
                    portal_locations[(j, i)] = f[i - 2][j] + f[i - 1][j]
                elif f[i + 1][j] in alphabet:
                    if f[i + 1][j] + f[i + 2][j] in portals:
                        portals[f[i + 1][j] + f[i + 2][j]].append((j, i))
                    else:
                        portals[f[i + 1][j] + f[i + 2][j]] = [(j, i)]
                    portal_locations[(j, i)] = f[i + 1][j] + f[i + 2][j]
                elif f[i][j - 1] in alphabet:
                    if f[i][j - 2] + f[i][j - 1] in portals:
                        portals[f[i][j - 2] + f[i][j - 1]].append((j, i))
                    else:
                        portals[f[i][j - 2] + f[i][j - 1]] = [(j, i)]
                    portal_locations[(j, i)] = f[i][j - 2] + f[i][j - 1]
                elif f[i][j + 1] in alphabet:
                    if f[i][j + 1] + f[i][j + 2] in portals:
                        portals[f[i][j + 1] + f[i][j + 2]].append((j, i))
                    else:
                        portals[f[i][j + 1] + f[i][j + 2]] = [(j, i)]
                    portal_locations[(j, i)] = f[i][j + 1] + f[i][j + 2]

    queue = deque()
    queue.append((portals["AA"][0], 0))
    seen = set()
    while queue:
        current_position, current_steps = queue.popleft()
        if current_position == portals["ZZ"][0]:
            print(current_steps)
            break
        if current_position in seen:
            continue
        seen.add(current_position)
        if current_position[0] > 0 and f[current_position[1]][current_position[0] - 1] == ".":
            queue.append(((current_position[0] - 1, current_position[1]), current_steps + 1))
        if current_position[0] < len(f[0]) - 1 and f[current_position[1]][current_position[0] + 1] == ".":
            queue.append(((current_position[0] + 1, current_position[1]), current_steps + 1))
        if current_position[1] > 0 and f[current_position[1] - 1][current_position[0]] == ".":
            queue.append(((current_position[0], current_position[1] - 1), current_steps + 1))
        if current_position[1] < len(f) - 1 and f[current_position[1] + 1][current_position[0]] == ".":
            queue.append(((current_position[0], current_position[1] + 1), current_steps + 1))
        if current_position in portal_locations and portal_locations[current_position] != "AA":
            queue.append((get_other_portal(portals, current_position, portal_locations[current_position]), current_steps + 1))


if __name__ == "__main__":
    main()
