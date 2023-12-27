"""Tests for AoC 6, 2023."""

# Standard library imports
import pathlib

# Third party imports
import aoc202306
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202306.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202306.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == [7, 15, 30]
    assert example1[1] == [9, 40, 200]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202306.part1(example1) == 288


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202306.part2(example1) == 71503
