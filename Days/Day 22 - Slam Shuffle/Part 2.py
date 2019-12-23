def main():
    f = [line.rstrip("\n").split(" ") for line in open("Data.txt")]
    offset_orig = 0
    increment_orig = 1
    offset, increment = offset_orig, increment_orig
    num_cards = 119315717514047
    num_times = 101741582076661
    for technique in f:
        if technique[0] == "cut":
            offset += increment*int(technique[1])
        elif technique[1] == "into":
            increment *= -1
            offset += increment
        elif technique[1] == "with":
            increment *= pow(int(technique[3]), num_cards - 2, num_cards)
        else:
            raise ValueError

    offset_diff, increment_mult = offset, increment
    increment = pow(increment_mult, num_times, num_cards)
    offset = offset_diff*pow(1 - increment_mult, num_cards - 2, num_cards)*(1 - pow(increment_mult, num_times, num_cards))
    print((offset + increment*2020) % num_cards)


if __name__ == "__main__":
    main()
