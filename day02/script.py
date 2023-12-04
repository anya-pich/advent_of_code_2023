import re

cubes_available = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = 8
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

        example_part_two = solve_part_two(input)
        answer = 2286
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    ids_total = 0
    for line in lines:
        game, hands = line.split(': ')
        game_no = game.split(' ')[-1]
        if all(is_valid(hand) for hand in hands.split(';')):
            ids_total += int(game_no)
    return ids_total

def is_valid(hand):
    for dice in hand.split(', '):
        count, color = dice.strip().split(' ')
        if int(count) > cubes_available[color]:
            return False
    return True

def solve_part_two(input):
    lines = input.splitlines()
    answer = 0
    for line in lines:
        game, hands = line.split(': ')
        counter = {
            'red': 0,
            'blue': 0,
            'green': 0
        }
        for hand in hands.split('; '):
            for dice in hand.split(', '):
                count, color = dice.strip().split(' ')
                if int(count) > counter[color]:
                    counter[color] = int(count)
        red, blue, green = counter.values()
        answer += red * blue * green
    return answer

main()
