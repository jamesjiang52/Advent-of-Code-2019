import math


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

    required = ["FUEL"]
    required_amounts = {"FUEL": 1}
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
        required_amounts[chemical] -= int(amount)*required_amount

    print(required_amounts["ORE"])


if __name__ == "__main__":
    main()
