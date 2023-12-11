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
			actualNumber, _ := strconv.Atoi(line[match[0]:match[1]])
			loc := Location{lineNumber, match[0], match[1] - 1}
			num := Number{actualNumber, loc}
			numbers = append(numbers, num)
		}
	}
	return numbers
}

// For each Number, check surrounding characters, including diagonals. If any surrounding char is a "symbol" add number to list of part numbers.
func identifyPartNumbers(numbers []Number, lines []string, numLines int, maxLineLength int) []int {
	var partNumbers []int
NumberLoop:
	for _, number := range numbers {
		//Bound search to line above and line below current number
		for row := number.Location.LineNumber - 1; row < number.Location.LineNumber+2; row++ {
			if row >= 0 && row < numLines {
				// Bound Search to character to left and right of number
				for column := number.Location.StartIndex - 1; column < number.Location.EndIndex+2; column++ {
					if column >= 0 && column < maxLineLength {
						// Check if it is a symbol (not a digit or '.')
						if !(unicode.IsDigit(rune(lines[row][column])) || lines[row][column] == '.') {
							partNumbers = append(partNumbers, number.Number)
							continue NumberLoop // Only add a part number once
						}
					}
				}
			}
		}
	}
	return partNumbers
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
	partNums := identifyPartNumbers(numLocs, lines, numLines, maxLineLength)
	fmt.Println(sumInts(partNums))

}
