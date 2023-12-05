import re

def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = 4361
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

        example_part_two = solve_part_two(input)
        answer = 467835
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    matrix = [line for line in lines]
    running_total = 0
    for y, row in enumerate(matrix):
        numbers = re.finditer(r'\d+', row)
        for number in numbers:
            if is_adjacent_to_symbol(number, matrix, y):
                running_total += int(number[0])
    return running_total

def is_adjacent_to_symbol(match, matrix, y):
    height = len(matrix)
    width = len(matrix[0])
    match_start, match_end = match.start(), match.end()
    x_start = 0 if match_start == 0 else match_start - 1
    x_end = match_end if match_end == width - 1 else match_end + 1
    y_start = 0 if y == 0 else y - 1
    y_end = y if y == height - 1 else y + 1
    pattern = re.compile("[^\d.\s]")
    for row_no in range(y_start, y_end + 1):
        symbol = pattern.search(matrix[row_no], x_start, x_end)
        if symbol:
            return True
    return False


def solve_part_two(input):
    lines = input.splitlines()
    matrix = [line for line in lines]
    running_total = 0
    for y, line in enumerate(lines):
        potential_gears = re.finditer(r'\*', line)
        for gear in potential_gears:
            running_total += get_gear_ratio(gear, matrix, y)
    return running_total

def get_gear_ratio(gear, matrix, y):
    height = len(matrix)
    width = len(matrix[0])
    gear_x = gear.start()
    numbers = []
    y_start = 0 if y == 0 else y - 1
    y_end = y if y == height - 1 else y + 1
    pattern = re.compile("\d+")
    for row_no in range(y_start, y_end + 1):
        row = matrix[row_no]
        matches = pattern.finditer(row)
        for match in matches:
            if not (match.start() > gear_x + 1 or match.end() - 1 < gear_x - 1):
                numbers.append(int(match[0]))
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    else:
        return 0

main()
