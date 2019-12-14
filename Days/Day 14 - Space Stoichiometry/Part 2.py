import math


def get_ore_amount(amount, reactions, chemical_lookup):
    required = ["FUEL"]
    required_amounts = {"FUEL": amount}
    while required:
        chemical = required.pop()
        amount, name = chemical_lookup[chemical]
        required_amount = math.ceil(required_amounts[chemical]/int(amount))
        for required_input in reactions[(amount, name)]:
            if required_input[1] in required_amounts:
                required_amounts[required_input[1]] += int(required_input[0])*required_amount
            else:
                required_amounts[required_input[1]] = int(required_input[0])*required_amount

            if required_input[1] != "ORE":
                required.append(required_input[1])
        required_amounts[chemical] -= int(amount)*required_amount  # excess

    return required_amounts["ORE"]


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    reactions = {}
    chemical_lookup = {}
    for reaction in f:
        pair = reaction.split(" => ")
        inputs = pair[0].split(", ")
        output = pair[1].split(" ")
        input_quantities = [tuple(input.split(" ")) for input in inputs]
        reactions[tuple(output)] = input_quantities
        chemical_lookup[output[1]] = tuple(output)

    low = 0
    high = 1000000000000//100000  # from part 1
    while low < high - 1:
        mid = (low + high)//2
        ore_amount = get_ore_amount(mid, reactions, chemical_lookup)
        if ore_amount < 1000000000000:
            low = mid
        elif ore_amount > 1000000000000:
            high = mid
        else:
            break

    print(low)


if __name__ == "__main__":
    main()
