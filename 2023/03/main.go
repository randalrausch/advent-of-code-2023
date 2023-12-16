////////////////////////////////////////////////////////////////
// Advent of Code 2023 Day 3
// https://adventofcode.com/2023/day/3
////////////////////////////////////////////////////////////////

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
	Value    int
	Location Location
}

// Given a slice of strings, return all numbers with their corresponding locations
func findNumbersAndLocations(lines []string) ([]Number, error) {
	re := regexp.MustCompile((`\d+`))
	var numbers []Number

	for lineNumber, line := range lines {
		matches := re.FindAllStringIndex(line, -1)
		for _, match := range matches {
			numberValue, err := strconv.Atoi(line[match[0]:match[1]])
			if err != nil {
				return nil, err
			}
			num := Number{numberValue, Location{lineNumber, match[0], match[1] - 1}}
			numbers = append(numbers, num)
		}
	}
	return numbers, nil
}

// checkSurroundings checks every adjacent position on the schematic to confirm if a number is a valid part number
// it also keeps track of the position of every asterisk found
func checkSurroundings(number Number, lines []string) (bool, [][2]int) {
	var asteriskPositions [][2]int
	isPartNumber := false

	for row := max(0, number.Location.LineNumber-1); row <= min(len(lines)-1, number.Location.LineNumber+1); row++ {
		for col := max(0, number.Location.StartIndex-1); col <= min(len(lines[row])-1, number.Location.EndIndex+1); col++ {
			character := lines[row][col]
			if !unicode.IsDigit(rune(character)) && character != '.' {
				isPartNumber = true
				if character == '*' {
					asteriskPositions = append(asteriskPositions, [2]int{row, col})
				}
			}
		}
	}
	return isPartNumber, asteriskPositions
}

// findGearRatiosAndPartNumbers identifies Gears and their ratios and Part Numbers
// Part Numbers are numbers with a symbol adjacent to the number
// A gear is any '*' symbol that is adjacent to exactly two part numbers. Gear ratios are the product of the two part numbers
func findGearRatiosAndPartNumbers(numbers []Number, lines []string) ([]int, []int) {
	var partNumbers, gearRatios []int
	potentialGears := make(map[[2]int][]int)

	for _, number := range numbers {
		isPartNumber, asteriskPositions := checkSurroundings(number, lines)
		if isPartNumber {
			partNumbers = append(partNumbers, number.Value)
			for _, pos := range asteriskPositions {
				potentialGears[pos] = append(potentialGears[pos], number.Value)
			}
		}
	}

	for _, parts := range potentialGears {
		if len(parts) == 2 {
			gearRatios = append(gearRatios, parts[0]*parts[1])
		}
	}
	return gearRatios, partNumbers
}

// Read input file and return slice of stings for each line
func readInput(filename string) ([]string, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	return lines, nil
}

// Apparently, it is idiomatic to create ones own sum function.
func sumInts(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}

// max returns the larger of two integers.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// min returns the smaller of two integers.
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	inputFile := "input.txt"

	lines, err := readInput(inputFile)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	numLocs, err := findNumbersAndLocations(lines)
	if err != nil {
		fmt.Println("Error finding numbers and locations:", err)
		return
	}

	gearRatios, partNums := findGearRatiosAndPartNumbers(numLocs, lines)
	fmt.Println("Sum of Part Numbers:", sumInts(partNums))
	fmt.Println("Sum of Gear Ratios:", sumInts(gearRatios))

}
