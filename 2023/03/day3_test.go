package main

import (
	"testing"
)

func TestDay3Part1(t *testing.T) {
	inputFile := "sample.txt"

	// Define the expected result
	expected := 4361

	// Call your module/package function
	lines, _ := readInput(inputFile)
	numLocs, _ := findNumbersAndLocations(lines)
	_, partNums := findGearRatiosAndPartNumbers(numLocs, lines)
	result := sumInts(partNums)

	// Check if the result matches the expected output
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}

func TestDay3Part2(t *testing.T) {
	inputFile := "sample.txt"

	// Define the expected result
	expected := 467835

	// Call your module/package function
	lines, _ := readInput(inputFile)
	numLocs, _ := findNumbersAndLocations(lines)
	gearRatios, _ := findGearRatiosAndPartNumbers(numLocs, lines)
	result := sumInts(gearRatios)

	// Check if the result matches the expected output
	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}
