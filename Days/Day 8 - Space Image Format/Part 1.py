def main():
    f = [line.rstrip("\n") for line in open("Data.txt")][0]
    width = 25
    height = 6
    depth = len(f)//(width*height)
    image = []
    image = [[[
        int(f[k + j*width + i*width*height]) for k in range(width)]
            for j in range(height)
        ]
        for i in range(depth)
    ]
    min_zeroes = width*height
    min_zeroes_layer = -1
    for layer in range(depth):
        count_zeroes = 0
        for i in range(height):
            for j in range(width):
                if not image[layer][i][j]:
                    count_zeroes += 1
        if count_zeroes < min_zeroes:
            min_zeroes = count_zeroes
            min_zeroes_layer = layer

    count_ones = 0
    count_twos = 0
    for i in range(height):
        for j in range(width):
            if image[min_zeroes_layer][i][j] == 1:
                count_ones += 1
            elif image[min_zeroes_layer][i][j] == 2:
                count_twos += 1
    print(count_ones*count_twos)


if __name__ == "__main__":
    main()
