# See https://adventofcode.com/2023/day/1

calibration_file = "./input1.txt"
debug_mode = False 
sum_of_calibrations = 0

if __name__ == "__main__":
    # Read Input File
    with open(calibration_file, 'r') as file:
        # Iterate through each line
        for line_number, line in enumerate(file, start=1):
            # Extract digits from the line
            digits = [char for char in line if char.isdigit()]

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
        
    print(f"The sum of all calibrations values is: {sum_of_calibrations}.")