"""AoC 5, 2023."""

# Standard library imports
import pathlib
import sys
import re


def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    maps = []
    seeds = [int(seed) for seed in re.findall(r'\d+', lines[0])]
    for line in lines[2:]:
        if 'map' in line:
            maps.append([])
        elif line != '':
            dest_start, src_start, range_len = [
                int(value) for value in line.split()]
            maps[-1].append((dest_start, src_start, range_len))
    return [seeds, maps]


def traverse_map(number, mapping):
    for dest_start, src_start, range_len in mapping:
        # check if the number falls within the source range.
        if src_start <= number < src_start+range_len:
            return number - src_start + dest_start
    # If the number is not in the map, it maps to itself.
    return number


def process_seed(seed, maps):
    result = seed
    for mapping in maps:
        result = traverse_map(result, mapping)
    return result


def part1(data):
    """Solve part 1."""
    seeds, maps = data
    locations = []
    for seed in seeds:
        locations.append(process_seed(seed, maps))
    return (min(locations))


def part2(data):
    """Solve part 2."""
    return 42


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
