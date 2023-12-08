# See https://adventofcode.com/2023/day/2
""" 
Determine which games would have been possible if the bag had been loaded 
with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?

Each game is listed with its ID number (like the 11 in Game 11: ...) 
followed by a semicolon-separated list of subsets of cubes that were 
revealed from the bag (like 3 red, 5 green, 4 blue).

My approach: For each line, check if any of the cube counts exceeds the threshold.
Use regular expressions to suck in the text.

"""
import re

# Setup
input_file = "./input2.txt"
debug_mode = False 
sum_of_gameIDs = 0

# Define a dictionary to store the cube color maximums
color_thresholds = {'green': 13, 'red': 12, 'blue': 14}

# Regular expression pattern to extract the "Game #:" part and the value-color pairs part
game_pattern = r'Game (\d+): (.*)'
# Regular expression pattern to find numbers followed by labels
color_pattern = r'(\d+) (\w+)'

if __name__ == "__main__":
    # Read Input File
    with open(input_file, 'r') as file:
        for line in file:                
            # Find the game ID and value-color pairs
            game_matches = re.search(game_pattern, line)
            if game_matches:
                game_id = int(game_matches.group(1))
                rest_of_line = game_matches.group(2)

                # Find all label-count pairs in bit after Game ID
                color_matches = re.findall(color_pattern, rest_of_line)

                 # Iterate through the cube color pairs and check if any exceed threshold
                valid_game = True
                for cubes, color in color_matches:
                    if int(cubes) > color_thresholds[color]:
                        if debug_mode:
                            print(f"Game #{game_id} is impossible.")
                            print(f"{line}")
                        valid_game = False
                        break
                if valid_game:
                    sum_of_gameIDs += game_id
            else:
                # Imagine input error handling here
                print("Invalid Syntax for Game ID.")

    print(f"Sum of possible game IDs = {sum_of_gameIDs}")