"""AoC 7, 2023."""

# Standard library imports
import pathlib
import sys
from collections import OrderedDict


def parse_data(puzzle_input):
    """Parse input."""
    data = []
    for line in puzzle_input.splitlines():
        parts = line.strip().split()  # Remove newline and split at space
        data.append((parts[0], int(parts[1])))

    return data


def parse_hand(hand):
    return [card for card in hand]


def count_ranks(ranks):
    """Dictionary Comprehension to count occurrences of each rank."""
    return {rank: ranks.count(rank) for rank in ranks}


def determine_hand(hand):
    ranks = parse_hand(hand)
    rank_counts = count_ranks(ranks)

    if 5 in rank_counts.values():
        return "Five of a Kind"
    elif 4 in rank_counts.values():
        return "Four of a Kind"
    elif sorted(rank_counts.values()) == [2, 3]:
        return "Full House"
    elif 3 in rank_counts.values():
        return "Three of a Kind"
    elif list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_counts.values():
        return "One Pair"
    else:
        return "High Card"


def determine_hand_jokers(hand):
    ranks = parse_hand(hand)
    rank_counts = count_ranks(ranks)

    # Jokers are wild
    for rank in rank_counts:
        if (rank == 'J'):
            num_jokers = rank_counts['J']
            for i in rank_counts:
                if i != 'J':
                    rank_counts[i] += num_jokers

    if 5 in rank_counts.values():
        return "Five of a Kind"
    elif 4 in rank_counts.values():
        return "Four of a Kind"
    # Handles normal full house and case of 2 pair and a joker
    elif sorted(rank_counts.values()) == [2, 3] or sorted(rank_counts.values()) == [1, 3, 3]:
        return "Full House"
    elif 3 in rank_counts.values():
        return "Three of a Kind"
    elif list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_counts.values():
        return "One Pair"
    else:
        return "High Card"


def card_strength(card):
    card_rank_strength = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return card_rank_strength[card]


def card_strength_jokers(card):
    card_rank_strength = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    return card_rank_strength[card]


def sort_games(games):
    if games:
        return sorted(games, key=lambda x: [card_strength(card) for card in x[0]])
    return []


def sort_games_jokers(games):
    if games:
        return sorted(games, key=lambda x: [card_strength_jokers(card) for card in x[0]])
    return []


def init_ordered_type_dict():
    """Initialize dictionary with empty lists. Keep order based on hand rank, lowest first."""
    hand_ranks = ["High Card", "One Pair", "Two Pair", "Three of a Kind",
                  "Full House", "Four of a Kind", "Five of a Kind"]
    games_by_type = OrderedDict()
    for key in hand_ranks:
        games_by_type[key] = []

    return games_by_type


def part1(data):
    """Solve part 1."""

    games_by_type = init_ordered_type_dict()

    # Iterate through games. Assign games to hand type category.
    for game in data:
        games_by_type[determine_hand(game[0])].append(game)

    # Sort hands within each game type
    sorted_games_by_type = OrderedDict()
    for type in games_by_type:
        sorted_games_by_type[type] = sort_games(games_by_type[type])

    # multiply bids times rank and sum it all up.
    total_winnings = 0
    rank = 1
    for type in sorted_games_by_type:
        for game in sorted_games_by_type[type]:
            total_winnings += game[1]*rank
            rank += 1

    return total_winnings


def part2(data):
    """Solve part 2."""

    games_by_type = init_ordered_type_dict()

    # Iterate through games. Assign games to hand type category.
    for game in data:
        games_by_type[determine_hand_jokers(game[0])].append(game)

    # Sort hands within each game type
    sorted_games_by_type = OrderedDict()
    for type in games_by_type:
        sorted_games_by_type[type] = sort_games_jokers(games_by_type[type])

    # multiply bids times rank and sum it all up.
    total_winnings = 0
    rank = 1
    for type in sorted_games_by_type:
        for game in sorted_games_by_type[type]:
            total_winnings += game[1]*rank
            rank += 1

    return total_winnings


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
