import re

def main():
    with open("example.txt") as f:
        input = f.read()

        example_part_one = solve_part_one(input)
        answer = 2
        assert example_part_one == answer, f"expected {answer}, got {example_part_one}"

    with open("example_two.txt") as f:
        input = f.read()

        example_two_part_one = solve_part_one(input)
        answer = 6
        assert example_two_part_one == answer, f"expected {answer}, got {example_two_part_one}"

    with open("example_three.txt") as f:
        input = f.read()

        example_part_two = solve_part_two(input)
        answer = 6
        assert example_part_two == answer, f"expected {answer}, got {example_part_two}"


    with open("input.txt") as f:
        input = f.read()

        answer_part_one = solve_part_one(input)
        print(f"{answer_part_one=}")

        answer_part_two = solve_part_two(input)
        print(f"{answer_part_two=}")


def solve_part_one(input):
    lines = input.splitlines()
    instructions, nodes = parse_map(lines)
    steps = 0
    i = 0
    node = nodes['AAA']
    while True:
        child = node[instructions[i]]
        steps += 1
        if child == 'ZZZ':
            break
        i = (i + 1) % len(instructions)
        node = nodes[child]
    return steps

def parse_map(lines):
    instructions = []
    for char in list(lines[0].strip()):
        instructions.append(0 if char == 'L' else 1)
    i = 2
    nodes = {}
    while i < len(lines):
        key, left, right = re.findall('\w{3}', lines[i])
        nodes[key] = [left, right]
        i += 1
    return instructions, nodes

def solve_part_two(input):
    lines = input.splitlines()
    instructions, node_map = parse_map(lines)
    steps = 0
    i = 0
    nodes = list(filter(lambda x: x[-1] == 'A', node_map.keys()))
    print(nodes)
    while True:
        steps += 1
        for k, node in enumerate(nodes):
            next_node = node_map[node][instructions[i]]
            nodes[k] = next_node
        if all(node[-1] == 'Z' for node in nodes):
            break
        i = (i + 1) % len(instructions)
    return steps

main()
