import re

def main():
    with open("input.txt") as f:
        input = f.read()

        example = """1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet"""

        example_part_one = solve_part_one(example)
        assert example_part_one == 142, f"expected 142, got {example_part_one}"

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        example2 = """two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen"""

        example_part_two = solve_part_two(example2)
        assert example_part_two == 281, f"expected 281, got {example_part_two}"

        example3 = "1eightwo"
        assert solve_part_two(example3) == 12, ""

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    total = 0
    for line in lines:
        first_digit = get_first_digit(line)
        if first_digit == None:
            throw('no digits')
        last_digit = get_last_digit(line)
        calibration_value = first_digit + last_digit
        total += int(calibration_value)
    return total

def get_first_digit(string):
    i = 0
    while i < len(string):
        if string[i].isdigit():
            return string[i]
        i += 1
    return None

def get_last_digit(string):
    i = len(string) - 1
    while i >= 0:
        if string[i].isdigit():
            return string[i]
        i -= 1
    return None

def solve_part_two(input):
    lines = input.splitlines()
    total = 0
    for line in lines:
        total += int(get_calibration_value(line))
    return total

def get_calibration_value(string):
    pattern = re.compile(r'one|two|three|four|five|six|seven|eight|nine|[1-9]')
    first_match = pattern.search(string)
    last_match = None
    i = len(string) - 1
    while i >= 0 and not last_match:
        last_match = pattern.match(string, i, len(string))
        i -= 1
    calibration_value = convert_word_to_digit(first_match[0]) + convert_word_to_digit(last_match[0])
    return calibration_value

def convert_word_to_digit(word):
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    if len(word) == 1:
        return word
    else:
        return word_to_number[word]

main()
