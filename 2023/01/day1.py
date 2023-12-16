###########################################################
# Advent of Code 2023 Day 1
# https://adventofcode.com/2023/day/1
###########################################################

import re

calibration_file = "./input1.txt"
debug_mode = False 
number_words = {
         "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
         "six": "6", "seven": "7", "eight": "8", "nine": "9" #, "zero": "0"
     }


def sum_calibrations(pattern):
    sum_of_calibrations = 0

    # Read Input File
    with open(calibration_file, 'r') as file:
        # Iterate through each line
        for line_number, line in enumerate(file, start=1):
            
            # Use this line if you don't want overlapping numbers (e.g. "twone" matches "two")
            # matches = re.findall(pattern, line, re.IGNORECASE)
            
            # Use these lines if you want overlapping numbers (e.g. "twone" matches ["two", "one"])
            matches = []
            for i in range(len(line)):
                match = re.match(pattern, line[i:], re.IGNORECASE)
                if match:
                    matches.append(match.group(0))

            digits = [number_words.get(match, match) for match in matches]

            if digits:
                # Combine the first and last digits if found
                two_digit_integer = int(digits[0] + digits[-1])
                
                # Sum 2-digit values with all previous values
                sum_of_calibrations += two_digit_integer
            else:
                # Imagine proper error handling here
                print(f"Warning: No digits found in line {line_number}")
                
            if debug_mode:
                print(f"Line #{line_number} is: {line.strip()}")
                print(f"The two digit number is: {two_digit_integer}")        
                print(f"The running sum is: {sum_of_calibrations}\n") 

    return sum_of_calibrations   

if __name__ == "__main__":
    
    # Part 1
    pattern = r'(\d)'
    sum_of_calibrations = sum_calibrations(pattern)
    print(f"Part 1: The sum of all calibration values is: {sum_of_calibrations}.")

    # Part 2
    pattern = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
    sum_of_calibrations = sum_calibrations(pattern)
    print(f"Part 2: The sum of all corrected calibration values is: {sum_of_calibrations}.")