def main():
    f = [line.rstrip("\n") for line in open("Data.txt")][0]
    width = 25
    height = 6
    depth = len(f)//(width*height)
    image = []
    image = [[[
        f[k + j*width + i*width*height] for k in range(width)]
            for j in range(height)
        ]
        for i in range(depth)
    ]
    actual_image = [["0"]*width for i in range(height)]
    for layer in range(depth):
        for i in range(height):
            for j in range(width):
                if actual_image[i][j] == "0":
                    if image[layer][i][j] == "0":
                        actual_image[i][j] = " "
                    elif image[layer][i][j] == "1":
                        actual_image[i][j] = "8"
    print("\n".join(["".join(row) for row in actual_image]))


if __name__ == "__main__":
    main()
