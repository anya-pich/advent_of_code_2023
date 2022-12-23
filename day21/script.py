def parse_input(input):
    lines = input.splitlines()
    dictionary = {}
    for line in lines:
        key, value = line.strip().split(": ")
        values = value.split(" ")
        if len(values) == 1:
            dictionary[key] = int(values[0])
        else:
            dictionary[key] = values
    return dictionary


def main():

    with open("example.txt") as f:
        input = f.read()
        dictionary = parse_input(input)

        example_part_one = solve_part_one("root", dictionary)
        assert example_part_one == 152, f"expected 152, got {example_part_one}"

        example_part_two = solve_part_two(dictionary)
        assert example_part_two == 301, f"expected 301, got {example_part_two}"

    with open("input.txt") as f:
        input = f.read()
        dictionary = parse_input(input)

        answer_part_one = solve_part_one("root", dictionary)
        print(f"{answer_part_one=}")

        # answer_part_two = solve_part_two(input)
        # print(f"{answer_part_two=}")


def solve_part_one(monkey, dictionary):
    if isinstance(dictionary[monkey], list):
        monkey_1, operator, monkey_2 = dictionary[monkey]
        value_1 = solve_part_one(monkey_1, dictionary)
        value_2 = solve_part_one(monkey_2, dictionary)
        return eval(f"{value_1} {operator} {value_2}")
    else:
        return dictionary[monkey]


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
