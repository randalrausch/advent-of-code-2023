// https://adventofcode.com/2023/day/3

package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode"
)

type Location struct {
	LineNumber int
	StartIndex int
	EndIndex   int
}

type Number struct {
	Number   int
	Location Location
}

// Given a slice of strings, return all numbers with their corresponding locations
func findNumbersAndLocations(lines []string) []Number {
	re := regexp.MustCompile((`\d+`))
	var numbers []Number

	for lineNumber, line := range lines {
		matches := re.FindAllStringIndex(line, -1)
		for _, match := range matches {
			actualNumber, err := strconv.Atoi(line[match[0]:match[1]])
			if err != nil {
				panic(err)
			}
			loc := Location{lineNumber, match[0], match[1] - 1}
			num := Number{actualNumber, loc}
			numbers = append(numbers, num)
		}
	}
	return numbers
}

// For each Number, check surrounding characters, including diagonals. If any surrounding char is a "symbol" add number to list of part numbers.
// A gear is any * symbol that is adjacent to exactly two part numbers
func identifyGearsAndPartNumbers(numbers []Number, lines []string, numLines int, maxLineLength int) ([]int, []int) {
	var partNumbers []int
	potentialGears := make(map[[2]int][]int)
	var gearRatios []int

	for _, number := range numbers {
		isPartNumber := false
		// Bound search to line above and line below current number
		for row := number.Location.LineNumber - 1; row <= number.Location.LineNumber+1; row++ {
			if row >= 0 && row < numLines {
				// Bound Search to character to left and right of number
				for column := number.Location.StartIndex - 1; column <= number.Location.EndIndex+1; column++ {
					if column >= 0 && column < maxLineLength {
						// Check if it is a symbol (not a digit or '.'), indicating the number in question is a partNumber
						charachter := lines[row][column]
						if !(unicode.IsDigit(rune(charachter)) || charachter == '.') {
							isPartNumber = true
							if charachter == '*' {
								potentialGears[[2]int{row, column}] = append(potentialGears[[2]int{row, column}], number.Number)
							}
						}
					}
				}
			}
		}
		if isPartNumber {
			partNumbers = append(partNumbers, number.Number)
		}
	}
	for _, parts := range potentialGears {
		if len(parts) == 2 {
			gearRatios = append(gearRatios, parts[0]*parts[1])
		}
	}
	return gearRatios, partNumbers
}

// Read input file and store height and width of input.
func readInput(filename string) ([]string, int, int) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	maxLineLength := 0
	for _, line := range lines {
		if len(line) > maxLineLength {
			maxLineLength = len(line)
		}
	}

	return lines, len(lines), maxLineLength
}

// Apparently, it is idiomatic to create ones own sum function.
func sumInts(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}

func main() {
	inputFile := "input.txt"

	lines, numLines, maxLineLength := readInput(inputFile)
	numLocs := findNumbersAndLocations(lines)
	gearRatios, partNums := identifyGearsAndPartNumbers(numLocs, lines, numLines, maxLineLength)
	fmt.Println(sumInts(partNums))
	fmt.Println(sumInts(gearRatios))
}
