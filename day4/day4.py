###########################################################
# Advent of Code 2023 Day 4
# https://adventofcode.com/2023/day/4
###########################################################

import re

input_file = "input.txt"
total_points = 0

if __name__ == "__main__":
    # Read Input File
    with open(input_file, 'r') as file:
        for line in file:
            card_value = 0
            # Parse each line into 3 parts. (identifier, winning_numbers, scratch_numbers)
            parts = re.split(r'[:|]', line, maxsplit=2)
            winning_numbers = set(re.findall(r'\d+', parts[1]))
            scratch_numbers = set(re.findall(r'\d+', parts[2]))
    
            match_count = sum(1 for number in winning_numbers if number in scratch_numbers)

            if match_count > 0:
                card_value = 2 ** (match_count-1)

            total_points += card_value

print(total_points)

