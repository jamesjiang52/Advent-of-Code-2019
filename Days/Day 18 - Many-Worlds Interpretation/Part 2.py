from collections import deque


def main():
    f = [list(line.rstrip("\n")) for line in open("Data.txt")]
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == "@":
                f[i][j] = "#"
                f[i + 1][j] = "#"
                f[i - 1][j] = "#"
                f[i][j + 1] = "#"
                f[i][j - 1] = "#"
                starting_positions = ((j - 1, i - 1), (j + 1, i - 1), (j - 1, i + 1), (j + 1, i + 1))

    keys = "abcdefghijklmnopqrstuvwxyz"
    doors = keys.upper()
    queue = deque()
    queue.append((starting_positions, 0, ""))
    seen = [set() for i in range(4)]
    while queue:
        current_positions, current_steps, current_keys = queue.popleft()
        current_positions = list(current_positions)
        if "".join(sorted(current_keys)) == keys:
            print(current_steps)
            return
        for i in range(4):
            current_position = current_positions[i]
            if (current_position, current_keys) in seen[i]:
                continue
            seen[i].add((current_position, current_keys))
            tmp_keys = current_keys
            if f[current_position[1]][current_position[0]] in keys and f[current_position[1]][current_position[0]] not in current_keys:
                current_keys += f[current_position[1]][current_position[0]]
                queue.appendleft((tuple(current_positions), current_steps, current_keys))
            elif f[current_position[1]][current_position[0]] in doors:
                if keys[doors.index(f[current_position[1]][current_position[0]])] not in current_keys:
                    continue
            if current_position[0] > 0 and f[current_position[1]][current_position[0] - 1] != "#":
                current_positions[i] = (current_position[0] - 1, current_position[1])
                queue.append((tuple(current_positions), current_steps + 1, current_keys))
                current_positions[i] = (current_position[0], current_position[1])
            if current_position[0] < len(f[0]) - 1 and f[current_position[1]][current_position[0] + 1] != "#":
                current_positions[i] = (current_position[0] + 1, current_position[1])
                queue.append((tuple(current_positions), current_steps + 1, current_keys))
                current_positions[i] = (current_position[0], current_position[1])
            if current_position[1] > 0 and f[current_position[1] - 1][current_position[0]] != "#":
                current_positions[i] = (current_position[0], current_position[1] - 1)
                queue.append((tuple(current_positions), current_steps + 1, current_keys))
                current_positions[i] = (current_position[0], current_position[1])
            if current_position[1] < len(f) - 1 and f[current_position[1] + 1][current_position[0]] != "#":
                current_positions[i] = (current_position[0], current_position[1] + 1)
                queue.append((tuple(current_positions), current_steps + 1, current_keys))
                current_positions[i] = (current_position[0], current_position[1])
            current_keys = tmp_keys


if __name__ == "__main__":
    main()
