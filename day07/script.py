from collections import Counter

def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = 6440
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

        example_part_two = solve_part_two(input)
        answer = 5905
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    hands = [line.split() for line in input.splitlines()]
    types = [[] for i in range(7)]
    for hand in hands:
        hand.append(translate_hand(hand[0]))
        card_count = dict(Counter(hand[0]))
        card_type = sorted(card_count.values(), reverse=True)
        if card_type[0] == 5:
            types[0].append(hand)
        elif card_type[0] == 4:
            types[1].append(hand)
        elif card_type[0] == 3 and card_type[1] == 2:
            types[2].append(hand)
        elif card_type[0] == 3:
            types[3].append(hand)
        elif card_type[0] == 2 and card_type[1] == 2:
            types[4].append(hand)
        elif card_type[0] == 2:
            types[5].append(hand)
        elif card_type[0] == 1:
            types[6].append(hand)
    hands_ranked = []
    for card_type in types:
        card_type.sort(key=lambda x: x[2])
        hands_ranked += card_type
    winnings = 0
    for i, card in enumerate(hands_ranked):
        points = (len(hands_ranked) - i) * int(card[1])
        winnings += points
    return winnings

def translate_hand(hand):
    value_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    mapping = {key: value for key, value in zip(value_order, letters)}
    return ''.join([mapping.get(char, char) for char in hand])


def solve_part_two(input):
    hands = [line.split() for line in input.splitlines()]
    types = [[] for i in range(7)]
    for hand in hands:
        hand.append(translate_hand_with_jokers(hand[0]))
        card_count = dict(Counter(hand[0]))
        sorted_count = dict(sorted(card_count.items(), key=lambda item: item[1], reverse=True))
        jokers = card_count.get('J', 0)
        if jokers > 0 and jokers < 5:
            print(sorted_count)
            jokers_count = sorted_count.pop('J')
            first_key = next(iter(sorted_count))
            sorted_count[first_key] += jokers_count
        card_type = list(sorted_count.values())
        if card_type[0] == 5:
            types[0].append(hand)
        elif card_type[0] == 4:
            types[1].append(hand)
        elif card_type[0] == 3 and card_type[1] == 2:
            types[2].append(hand)
        elif card_type[0] == 3:
            types[3].append(hand)
        elif card_type[0] == 2 and card_type[1] == 2:
            types[4].append(hand)
        elif card_type[0] == 2:
            types[5].append(hand)
        elif card_type[0] == 1:
            types[6].append(hand)
    hands_ranked = []
    for card_type in types:
        card_type.sort(key=lambda x: x[2])
        hands_ranked += card_type
    winnings = 0
    for i, card in enumerate(hands_ranked):
        points = (len(hands_ranked) - i) * int(card[1])
        winnings += points
    return winnings

def translate_hand_with_jokers(hand):
    value_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    mapping = {key: value for key, value in zip(value_order, letters)}
    return ''.join([mapping.get(char, char) for char in hand])


main()
