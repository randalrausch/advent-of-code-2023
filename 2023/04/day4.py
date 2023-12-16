###########################################################
# Advent of Code 2023 Day 4
# https://adventofcode.com/2023/day/4
###########################################################

import re
from collections import defaultdict

total_points = 0
total_cards = 0
card_instances = defaultdict(lambda: 1) # Initialize number of each card type to be 1. (the originals)

if __name__ == "__main__":
    # Read Input File
    with open("input.txt", 'r') as file:
        for index, line in enumerate(file, start=1):
            card_value = 0
            # Parse each line into 3 parts. (card_label, winning_numbers, scratch_numbers)
            parts = re.split(r'[:|]', line, maxsplit=2)
            winning_numbers = [int(x) for x in parts[1].split()]
            scratch_numbers = [int(x) for x in parts[2].split()]
            match_count = len(set(winning_numbers) & set(scratch_numbers))            

            # Calculate points
            if match_count > 0:
                card_value = 2 ** (match_count-1)
                total_points += card_value

            # Processing winnings (create card copies)
            for j in range(match_count):
                card_instances[index+j+1] += card_instances[index]
                # Note: Defaultdict behavior prevents indexing out of range errors. 
                # Also, this will create copies of non-existant cards beyond the end of the file,
                # but they won't be summed as the next statement stops adding on the last line of the input file.
            total_cards += card_instances[index]

print("The total number of points is: ", total_points)
print("The total number of cards is: ", total_cards)