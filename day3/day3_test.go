package main

import (
	"testing"
)

func TestDay3Part1(t *testing.T) {
	inputFile := "sample.txt"

	// Define the expected result
	expected := 4361

	// Call your module/package function
	lines, numLines, maxLineLength := readInput(inputFile)
	numLocs := findNumbersAndLocations(lines)
	partNums := identifyPartNumbers(numLocs, lines, numLines, maxLineLength)
	result := sumInts(partNums)

	// Check if the result matches the expected output
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}
