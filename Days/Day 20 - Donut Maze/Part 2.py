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
    outer_portal_locations = {}
    inner_portal_locations = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == ".":
                if f[i - 1][j] in alphabet:
                    if f[i - 2][j] + f[i - 1][j] in portals:
                        portals[f[i - 2][j] + f[i - 1][j]].append((j, i))
                    else:
                        portals[f[i - 2][j] + f[i - 1][j]] = [(j, i)]
                    if i == 2:
                        outer_portal_locations[(j, i)] = f[i - 2][j] + f[i - 1][j]
                    else:
                        inner_portal_locations[(j, i)] = f[i - 2][j] + f[i - 1][j]
                elif f[i + 1][j] in alphabet:
                    if f[i + 1][j] + f[i + 2][j] in portals:
                        portals[f[i + 1][j] + f[i + 2][j]].append((j, i))
                    else:
                        portals[f[i + 1][j] + f[i + 2][j]] = [(j, i)]
                    if i == len(f) - 3:
                        outer_portal_locations[(j, i)] = f[i + 1][j] + f[i + 2][j]
                    else:
                        inner_portal_locations[(j, i)] = f[i + 1][j] + f[i + 2][j]
                elif f[i][j - 1] in alphabet:
                    if f[i][j - 2] + f[i][j - 1] in portals:
                        portals[f[i][j - 2] + f[i][j - 1]].append((j, i))
                    else:
                        portals[f[i][j - 2] + f[i][j - 1]] = [(j, i)]
                    if j == 2:
                        outer_portal_locations[(j, i)] = f[i][j - 2] + f[i][j - 1]
                    else:
                        inner_portal_locations[(j, i)] = f[i][j - 2] + f[i][j - 1]
                elif f[i][j + 1] in alphabet:
                    if f[i][j + 1] + f[i][j + 2] in portals:
                        portals[f[i][j + 1] + f[i][j + 2]].append((j, i))
                    else:
                        portals[f[i][j + 1] + f[i][j + 2]] = [(j, i)]
                    if j == len(f[i]) - 3:
                        outer_portal_locations[(j, i)] = f[i][j + 1] + f[i][j + 2]
                    else:
                        inner_portal_locations[(j, i)] = f[i][j + 1] + f[i][j + 2]

    queue = deque()
    queue.append((portals["AA"][0], 0, 0))
    seen = set()
    while queue:
        current_position, current_steps, current_level = queue.popleft()
        if current_position == portals["ZZ"][0] and not current_level:
            print(current_steps)
            break
        if (current_position, current_level) in seen:
            continue
        seen.add((current_position, current_level))
        if current_position[0] > 0 and f[current_position[1]][current_position[0] - 1] == ".":
            queue.append(((current_position[0] - 1, current_position[1]), current_steps + 1, current_level))
        if current_position[0] < len(f[0]) - 1 and f[current_position[1]][current_position[0] + 1] == ".":
            queue.append(((current_position[0] + 1, current_position[1]), current_steps + 1, current_level))
        if current_position[1] > 0 and f[current_position[1] - 1][current_position[0]] == ".":
            queue.append(((current_position[0], current_position[1] - 1), current_steps + 1, current_level))
        if current_position[1] < len(f) - 1 and f[current_position[1] + 1][current_position[0]] == ".":
            queue.append(((current_position[0], current_position[1] + 1), current_steps + 1, current_level))
        if current_position in outer_portal_locations and outer_portal_locations[current_position] not in ["AA", "ZZ"]:
            if current_level == 0:
                pass
            else:
                queue.append((get_other_portal(portals, current_position, outer_portal_locations[current_position]), current_steps + 1, current_level - 1))
        elif current_position in inner_portal_locations:
            queue.append((get_other_portal(portals, current_position, inner_portal_locations[current_position]), current_steps + 1, current_level + 1))


if __name__ == "__main__":
    main()
