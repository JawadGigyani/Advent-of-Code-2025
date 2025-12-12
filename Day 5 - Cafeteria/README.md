# Advent of Code 2025 - Day 5: Cafeteria

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/5)

## 🍽️ Problem Description

In the Cafeteria, the Elves are struggling with a new inventory management system. The system provides a list of fresh ingredient ID ranges and a list of available ingredient IDs. The challenge is to determine which available IDs are fresh and, in a second part, to count all IDs that are considered fresh by the ranges.

### Part 1

Given a set of inclusive fresh ingredient ID ranges (which may overlap) and a list of available ingredient IDs, the program must count how many available IDs are fresh (i.e., fall within any of the ranges).

### Part 2

The available ingredient IDs are ignored. Instead, the task is to count all unique ingredient IDs that are considered fresh by the ranges (i.e., the total number of IDs covered by the union of all ranges).

## 🧠 Solution Logic

The solution is implemented in **Python** and efficiently handles large ranges and IDs.

### Key Concept: Merging Ranges

- All fresh ID ranges are parsed and merged into a sorted, non-overlapping list.
- For Part 1, each available ID is checked using binary search to see if it falls within any merged range.
- For Part 2, the total number of unique fresh IDs is calculated by summing the lengths of all merged ranges.

### Implementation

- **Input:**
  - The first section of `input.txt` contains fresh ID ranges (one per line, e.g., `3-5`).
  - A blank line separates the ranges from the available IDs (one per line).
- **Output:**
  - Part 1: The number of available IDs that are fresh.
  - Part 2: The total number of unique fresh IDs covered by the ranges.

#### Main Functions

- Merges overlapping/adjacent ranges for efficient lookup and counting.
- Uses binary search for fast ID checks in Part 1.

## 🚀 How to Run

1. Place the puzzle input in `input.txt` (ranges, blank line, then available IDs).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — The puzzle input.
