"""AoC 9, 2023."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    data = []
    for line in puzzle_input.splitlines():
        data.append([int(num) for num in line.split()])
    return data


def seq_differences(list_of_seq):
    last_seq = list_of_seq[-1]

    differences = [j - i for i, j in zip(last_seq, last_seq[1:])]
    list_of_seq.append(differences)

    # base case: all nunmbers are the same
    all_same = all(d == differences[0] for d in differences)
    if all_same:
        return list_of_seq
    # Otherwise, recursively add to list
    else:
        return seq_differences(list_of_seq)


def extrapolate(list_of_diffs):

    num_lists = len(list_of_diffs)

    if num_lists < 2:
        print("Bad Input")
        return None

    # Add the last value of the last list to the last value of the second to last list
    extrapolated_val = list_of_diffs[-1][-1] + list_of_diffs[-2][-1]

    if len(list_of_diffs) == 2:
        return extrapolated_val
    else:
        list_of_diffs[-2].append(extrapolated_val)
        list_of_diffs.pop()
        return extrapolate(list_of_diffs)


def reverse_extrap(list_of_diffs):

    num_lists = len(list_of_diffs)

    if num_lists < 2:
        print("Bad Input")
        return None

    # calculate first item in 2nd to last list minus first item from last list
    rev_exap_val = list_of_diffs[-2][0] - list_of_diffs[-1][0]

    if num_lists == 2:
        return rev_exap_val
    else:
        # preppend value to 2nd to last row
        list_of_diffs[-2] = [rev_exap_val] + list_of_diffs[-2]
        list_of_diffs.pop()
        return reverse_extrap(list_of_diffs)


def part1(data):
    """Solve part 1."""
    predictions = []
    for numbers in data:
        predictions.append(extrapolate(seq_differences([numbers])))
    return (sum(predictions))


def part2(data):
    """Solve part 2."""
    predictions = []
    for numbers in data:
        predictions.append(reverse_extrap(seq_differences([numbers])))
    return (sum(predictions))


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
