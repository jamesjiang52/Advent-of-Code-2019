from collections import deque


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == "@":
                starting_position = (j, i)

    keys = "abcdefghijklmnopqrstuvwxyz"
    doors = keys.upper()
    queue = deque()
    queue.append((starting_position, 0, ""))
    seen = set()
    while queue:
        current_position, current_steps, current_keys = queue.popleft()
        if current_keys == keys:
            print(current_steps)
            break
        if (current_position, current_keys) in seen:
            continue
        seen.add((current_position, current_keys))
        if f[current_position[1]][current_position[0]] in keys and f[current_position[1]][current_position[0]] not in current_keys:
            current_keys += f[current_position[1]][current_position[0]]
            current_keys = "".join(sorted(current_keys))
            queue.appendleft((current_position, current_steps, current_keys))
        elif f[current_position[1]][current_position[0]] in doors:
            if keys[doors.index(f[current_position[1]][current_position[0]])] not in current_keys:
                continue
        if current_position[0] > 0 and f[current_position[1]][current_position[0] - 1] != "#":
            queue.append(((current_position[0] - 1, current_position[1]), current_steps + 1, current_keys))
        if current_position[0] < len(f[0]) - 1 and f[current_position[1]][current_position[0] + 1] != "#":
            queue.append(((current_position[0] + 1, current_position[1]), current_steps + 1, current_keys))
        if current_position[1] > 0 and f[current_position[1] - 1][current_position[0]] != "#":
            queue.append(((current_position[0], current_position[1] - 1), current_steps + 1, current_keys))
        if current_position[1] < len(f) - 1 and f[current_position[1] + 1][current_position[0]] != "#":
            queue.append(((current_position[0], current_position[1] + 1), current_steps + 1, current_keys))


if __name__ == "__main__":
    main()
