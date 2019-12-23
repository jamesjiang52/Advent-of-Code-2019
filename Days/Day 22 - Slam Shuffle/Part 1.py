from collections import deque


def main():
    f = [line.rstrip("\n").split(" ") for line in open("Data.txt")]
    num_cards = 10007
    deck = deque(range(num_cards))
    for technique in f:
        if technique[0] == "cut":
            amount = int(technique[1])
            deck = deque(list(deck)[amount:] + list(deck)[0:amount])
        elif technique[1] == "into":
            deck.reverse()
        elif technique[1] == "with":
            new_deck = deque([0]*len(deck))
            for i in range(num_cards):
                new_deck[(i*int(technique[3])) % num_cards] = deck[i]
            deck = new_deck
        else:
            raise ValueError

    for i in range(len(deck)):
        if deck[i] == 2019:
            print(i)
            break


if __name__ == "__main__":
    main()
