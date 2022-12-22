def main():
    with open("input.txt") as f:
        input = f.read()

        example = """
            1000
            2000
            3000

            4000

            5000
            6000

            7000
            8000
            9000

            10000"""

        example_part_one = solve_part_one(example)
        assert example_part_one == 24000, f"expected 2400, got {example_part_one}"

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        example_part_two = solve_part_two(example)
        assert example_part_two == 45000, f"expected 45000, got {example_part_two}"

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    global_max = 0
    local_max = 0
    for line in lines:
        if line == "":
            global_max = max([global_max, local_max])
            local_max = 0
        else:
            local_max += int(line)
    answer = max([global_max, local_max])
    return answer


def solve_part_two(input):
    lines = input.splitlines()
    totals = []
    total = 0
    for line in lines:
        if line == "":
            totals.append(total)
            total = 0
        else:
            total += int(line)
    totals.append(total)
    totals.sort()
    answer = sum(totals[-3:])
    return answer


main()
