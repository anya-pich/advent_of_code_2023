def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = None
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

        example_part_two = solve_part_two(input)
        answer = None
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    return 0


def solve_part_two(input):
    return 0

main()
