def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = 288
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

        example_part_two = solve_part_two(input)
        answer = 71503
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    times = list(map(int, lines[0].split(':')[1].strip().split()))
    records = list(map(int, lines[1].split(':')[1].strip().split()))

    answer = 1
    for time, record in zip(times, records):
        wins = 0
        for wait in range(1, time):
            travel = wait * (time - wait)
            if travel > record:
                wins += 1
        answer *= wins
    return answer


def solve_part_two(input):
    lines = input.splitlines()
    time = int(''.join(lines[0].split(':')[1].split()))
    record = int(''.join(lines[1].split(':')[1].split()))

    min_wait = 1
    max_wait = time - 1
    while True:
        travel = min_wait * (time - min_wait)
        if travel > record:
            break
        min_wait += 1
    while True:
        travel = max_wait * (time - max_wait)
        if travel > record:
            break
        max_wait -= 1
    return max_wait - min_wait + 1

main()
