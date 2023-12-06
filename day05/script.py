def main():
    with open("example.txt", "r") as file:
        example_part_one = solve_part_one(file)
        answer = 35
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

    with open("example.txt", "r") as file:
        example_part_two = solve_part_two(file)
        answer = 46
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"

    with open("input.txt", "r") as file:
        answer_part_one = solve_part_one(file)
        print(f"{answer_part_one=}")

    with open("input.txt", "r") as file:
        answer_part_two = solve_part_two(file)
        print(f"{answer_part_two=}")


def solve_part_one(file):
    start_list = list(map(int, file.readline().strip().split(': ')[1].split(' ')))
    end_list = start_list.copy()
    skip_next = False
    for line in file:
        if skip_next:
            # we're in a map title
            skip_next = False
            continue
        content=line.strip()
        if not content:
            # we're in a new line between different maps
            start_list = end_list.copy()
            skip_next = True
            continue
        destination, source, range_length = [int(num) for num in content.split()]
        delta = destination - source
        for i, value in enumerate(start_list):
            if value >= source and value < source + range_length:
                end_list[i] = value + delta
    return min(end_list)

def solve_part_two(file):
    lines = file.readlines()
    seeds = list(map(int, lines[0].strip().split(': ')[1].split(' ')))
    seed_ranges = []
    for i in range(0, len(seeds) - 1, 2):
        start = seeds[i]
        end = seeds[i] + seeds[i+1] - 1
        seed_ranges.append([start,end])
    seed_ranges.sort(key=lambda x: x[0])

    value_ranges = seed_ranges
    transmuted_ranges = []
    almanac = parse_almanac(lines)
    for step in almanac:
        v, s = 0, 0
        while s < len(step) and v < len(value_ranges):
            v_start, v_end = value_ranges[v]
            s_start, s_end, s_delta = step[s]
            if v_end < s_start:
                transmuted_ranges.append(value_ranges[v])
                v += 1
            elif v_start > s_end:
                s += 1
            else:
                overlap_start = max(v_start, s_start)
                overlap_end = min(v_end, s_end)
                if v_start < overlap_start:
                    transmuted_ranges.append([v_start, overlap_start - 1])
                transmuted_ranges.append([overlap_start + s_delta, overlap_end + s_delta])
                if v_end > overlap_end:
                    value_ranges[v][0] = overlap_end + 1
                    s += 1
                else:
                    v += 1
        if v < len(value_ranges) - 1:
            transmuted_ranges += value_ranges[v:]
        transmuted_ranges.sort(key=lambda x: x[0])
        value_ranges = [transmuted_ranges[0]]
        # merge overlapping ranges
        i = 1
        while i < len(transmuted_ranges):
            if value_ranges[-1][1] >= transmuted_ranges[i][0] - 1:
                value_ranges[-1][1] = transmuted_ranges[i][1]
            else:
                value_ranges.append(transmuted_ranges[i])
            i += 1
        transmuted_ranges = []

    return value_ranges[0][0]

def parse_almanac(lines):
    steps = []
    step = []
    i = 3
    while i < len(lines):
        content = lines[i].strip()
        if not content:
            steps.append(sorted(step, key=lambda x: x[0]))
            step = []
            i += 2
            continue
        destination, source, range_length = [int(num) for num in content.split()]
        step.append((source, source + range_length - 1, destination - source))
        i += 1
    steps.append(sorted(step, key=lambda x: x[0]))
    return steps

# def solve_part_two(file):
#     lines = file.readlines()

#     # parse seeds
#     seed_ranges = list(map(int, lines[0].strip().split(': ')[1].split(' ')))
    
#     # parse almanac
#     steps = []
#     step = []
#     i = 3
#     while i < len(lines):
#         content = lines[i].strip()
#         if not content:
#             steps.append(step)
#             step = []
#             i += 2
#             continue
#         conversion = [int(num) for num in content.split()]
#         step.append(conversion)
#         i += 1
#     steps.append(step)

#     # translate seeds
#     min_location = None
#     for i in range(0, len(seed_ranges), 2):
#         range_start = seed_ranges[i]
#         range_length = seed_ranges[i+1]
#         for seed in range(range_start, range_start + range_length):
#             location = translate(seed, steps)
#             min_location = location if min_location is None else min(min_location, location)

#     return min_location

# def translate(seed, steps):
#     value = seed
#     for step in steps:
#         for destination, source, range_length in step:
#             if value >= source and value < source + range_length:
#                 value += (destination - source)
#                 break
#     return value

main()
