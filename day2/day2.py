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
sum_of_gameIDs = 0
sum_of_game_powers = 0

# Define a dictionary to store the cube color maximums
color_thresholds = {'green': 13, 'red': 12, 'blue': 14}

# Regular expression pattern to extract the "Game #:" part and split rest of line
game_pattern = r'Game (\d+): (.*)'
# Regular expression pattern to find numbers followed by labels
color_pattern = r'(\d+) (\w+)'

if __name__ == "__main__":
    # Read Input File
    with open(input_file, 'r') as file:
        for line in file:                
            # Find the game ID and cube-color pairs
            game_matches = re.search(game_pattern, line)
            if game_matches:
                game_id = int(game_matches.group(1))
                rest_of_line = game_matches.group(2)

                # Find all cube-color pairs in bit after Game ID
                color_matches = re.findall(color_pattern, rest_of_line)

                # Iterate through the cube-color pairs and check if any exceed threshold
                valid_game = True
                game_max_cubes = {'green': 0, 'red': 0, 'blue': 0}
                game_power=1 # identity value for multiplication
                for cubes, color in color_matches:
                    cubes = int(cubes)
                    if color in game_max_cubes and cubes > game_max_cubes[color]:
                        game_max_cubes[color] = cubes
            
                for color, max_cubes in game_max_cubes.items():
                    game_power *= max_cubes
                    if max_cubes > color_thresholds[color]:
                        valid_game = False
                if valid_game:
                    sum_of_gameIDs += game_id
                sum_of_game_powers += game_power
            else:
                # Imagine input error handling here
                print("Invalid Syntax for Game ID.")

    print(f"Sum of possible game IDs = {sum_of_gameIDs}")
    print(f"Sum of game powers = {sum_of_game_powers}")