"""AoC 6, 2023."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input into a list of lists of integers.

    Args:
        puzzle_input (str): Multiline string input where each line starts with a label followed by integers.

    Returns:
        List[List[int]]: A list of lists containing integers from each line of the input after a ":"
    """
    return [[int(x) for x in line.split()[1:]] for line in puzzle_input.splitlines() if line]


def calculate_distance(hold_time, race_duration):
    """Calculate the distance traveled based on hold time and race duration."""
    if 0 < hold_time < race_duration:
        return (race_duration - hold_time) * hold_time
    return 0


def ways_to_win(race_time, record):
    """Calculate the number of ways to win given the race time and record."""
    return sum(calculate_distance(time, race_time) > record for time in range(race_time))


def part1(data):
    """Calculate the product of the number of ways to win for each time in the dataset in a naive brute force way.

    Args:
        data (list): A list containing two lists - [times, records]

    Returns:
        int: The product of ways to win for each time.
    """
    times, records = data
    margin = 1
    for i, time in enumerate(times):
        margin *= ways_to_win(time, records[i])
    return margin


def part2(old_syntax):
    """Solve part 2 by concatenating lists of integers into single integers and finding ways to win.

    Args:
        data (list): A list containing two lists - [times, records]

    Returns:
        int: The number ways to win for the new syntax (ignoring spaces between digits)

    note: Naive brute force seems sufficient.
    """
    time = int(''.join(map(str, old_syntax[0])))
    distance = int(''.join(map(str, old_syntax[1])))
    return ways_to_win(time, distance)


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
