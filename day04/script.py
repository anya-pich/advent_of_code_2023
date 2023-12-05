def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = 13
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

        example_part_two = solve_part_two(input)
        answer = 30
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    running_total = 0
    for line in lines:
        _, numbers = line.split(': ')
        win_nums, scratch_nums = [nums.split() for nums in numbers.split(' | ')]
        overlap = [num for num in scratch_nums if num in win_nums]
        points = 2 ** (len(overlap) - 1) if len(overlap) else 0
        running_total += points
    return running_total


def solve_part_two(input):
    lines = input.splitlines()
    cards = [1 for card in lines]
    for i, line in enumerate(lines):
        _, numbers = line.split(': ')
        win_nums, scratch_nums = [nums.split() for nums in numbers.split(' | ')]
        overlap = [num for num in scratch_nums if num in win_nums]
        copies = cards[i]
        for point in range(len(overlap)):
            if i + point + 1 < len(cards):
                cards[i + point + 1] += copies
    return sum(cards)

main()
