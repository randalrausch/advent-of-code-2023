"""AoC 8, 2023."""

# Standard library imports
import itertools
import pathlib
import sys
import math


def parse_data(puzzle_input):
    """Parse input."""
    data = [[], {}]

    lines = puzzle_input.splitlines()

    # Grab the first line of R/L instructions
    data[0] = list(lines[0]) if lines else None

    for line in lines:
        line = line.strip()
        if line and "=" in line:
            key, value = line.split(' = ')
            value_tuple = tuple(value.strip('()').split(', '))
            data[1][key] = value_tuple

    return data


def find_next_element(instruction, node):
    if instruction == "L":
        return node[0]
    elif instruction == "R":
        return node[1]
    else:
        print("Bad Instruction")
        return None


def part1(data):
    """Solve part 1."""
    steps = 0
    current_key = "AAA"
    found_zzz = False
    instruction_list_iterations = 0

    if not any("ZZZ" in node for node in data[1].values()):
        print("Don't bother looking for something that isn't there")
        return None

    # Continue to iterate through instruction list until "ZZZ" is found
    while not found_zzz:
        for instruction in data[0]:
            steps += 1
            # Look up next element
            next_element = find_next_element(instruction, data[1][current_key])

            if next_element == "ZZZ":
                found_zzz = True
                break  # break out of for loop

            current_key = next_element

        if instruction_list_iterations > 10000:  # Avoid infinite loops. 10000 is arbitrary
            print(
                "Seems like you are in an infinite loop. Check you input and algorithm.")
            break
        instruction_list_iterations += 1
    return steps


def part2(data):
    """Solve part 2."""
    instructions, nodes = data
    # Find all starting nodes (ending in "A")
    starting_nodes = [node for node in nodes if node.endswith("A")]

    # Solve part 1 for each starting node (for nodes that end in "Z")
    loops = []
    for node in starting_nodes:
        steps = 0
        current_key = node
        cycler = itertools.cycle(instructions)
        while not current_key.endswith("Z"):
            steps += 1
            current_key = find_next_element(next(cycler), nodes[current_key])
        loops.append(steps)

    # Find Least common multiple of loop steps
    return math.lcm(*loops)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
