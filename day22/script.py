def parse_input(input):
    lines = input.readlines()
    matrix = []
    for line in lines:
        matrix.append(list(line.strip("\n")))

    instructions = matrix.pop()
    matrix.pop()

    directions = []
    num = ""
    for char in instructions:
        if char not in ["R", "L"]:
            num += char
        else:
            directions.append(int(num))
            directions.append(char)
            num = ""
    if num != "":
        directions.append(int(num))

    return matrix, directions


def main():

    with open("example.txt") as input:
        matrix, instructions = parse_input(input)

        example_part_one = solve_part_one(matrix, instructions)
    #     assert example_part_one == 152, f"expected 152, got {example_part_one}"

    #     example_part_two = solve_part_two(dictionary)
    #     assert example_part_two == 301, f"expected 301, got {example_part_two}"

    # with open("input.txt") as f:
    #     input = f.read()
    #     dictionary = parse_input(input)

    #     answer_part_one = solve_part_one("root", dictionary)
    #     print(f"{answer_part_one=}")

    #     # answer_part_two = solve_part_two(input)
    #     # print(f"{answer_part_two=}")


def solve_part_one(matrix, instructions):
    y = 0
    x = matrix[1].index(".")


def solve_part_two(dictionary):
    def calculate(monkey):
        if isinstance(dictionary[monkey], list):
            monkey_1, operator, monkey_2 = dictionary[monkey]
            value_1 = solve_part_one(monkey_1, dictionary)
            value_2 = solve_part_one(monkey_2, dictionary)
            return eval(f"{value_1} {operator} {value_2}")
        else:
            return dictionary[monkey]


main()
