# Advent of Code 2025 - Day 4: Printing Department

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/4)

## 🖨️ Problem Description

In the Printing Department, the Elves are surrounded by large rolls of paper, each represented by an `@` on a grid. The forklifts can only access a roll of paper if there are fewer than four other rolls in the eight adjacent positions. The challenge is to determine how many rolls are accessible and, in a second part, how many can be removed if the process is repeated until no more rolls can be accessed.

### Part 1

For each roll of paper (`@`), the program checks its eight neighbors. If fewer than four of those neighbors are also `@`, the roll is considered accessible. The task is to count all such accessible rolls in the initial grid.

### Part 2

After accessible rolls are removed, new rolls may become accessible. The process is repeated: in each round, all currently accessible rolls are removed, and the count is updated. This continues until no more rolls can be accessed. The goal is to determine the total number of rolls that can be removed through this iterative process.

## 🧠 Solution Logic

The solution is implemented in **Python** using **NumPy** and **SciPy** for efficient grid operations.

### Key Concept: Neighbor Counting with Convolution

- The grid is converted to a NumPy array, with `1` for `@` and `0` for `.`.
- A 3x3 convolution kernel is used to count the number of adjacent rolls for each cell.
- For Part 1, accessible rolls are those with fewer than four neighbors.
- For Part 2, the process is repeated, removing accessible rolls in each round until no more can be removed.

### Implementation

- **Input:** Each line in `input.txt` is a row of the grid.
- **Output:**
  - Part 1: The number of accessible rolls in the initial grid.
  - Part 2: The total number of rolls that can be removed through repeated rounds.

#### Main Functions

- Uses NumPy arrays and SciPy's `convolve2d` for efficient neighbor counting and grid updates.
- Loops through rounds, updating the grid and counting removed rolls until no more can be accessed.

## 🚀 How to Run

1. Place the puzzle input in `input.txt` (one grid row per line).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — The puzzle input grid.
