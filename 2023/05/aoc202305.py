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


def expand_seed_list(old_syntax_seeds):
    # Slice the list and parse the pairs
    seed_pairs = [old_syntax_seeds[i:i + 2]
                  for i in range(0, len(old_syntax_seeds), 2)]
    # Expand the list based on pair syntax
    seeds = [seed for pair in seed_pairs for seed in range(
        pair[0], pair[0]+pair[1])]

    return seeds


def part1(data):
    """Solve part 1."""
    seeds, maps = data
    locations = []
    for seed in seeds:
        locations.append(process_seed(seed, maps))
    return (min(locations))


def part2(data):
    """Solve part 2."""
    old_syntax_seeds, maps = data
    # expand seed list based on new range information
    seeds = expand_seed_list(old_syntax_seeds)

    # Brute force through this much longer list.
    locations = []
    for seed in seeds:
        locations.append(process_seed(seed, maps))
    return (min(locations))


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
