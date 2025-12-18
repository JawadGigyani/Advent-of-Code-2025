# Advent of Code 2025 - Day 9: Movie Theater

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/9)

## 🎬 Problem Description

In the Movie Theater, the protagonist encounters a tiled floor with a unique pattern. The Elves are redecorating by switching out some of the square tiles, and they provide a list of red tile coordinates. The challenge is to find the largest rectangle that uses red tiles as two of its opposite corners, with additional constraints in Part 2.

### Part 1

Given a list of red tile coordinates, the program must find the largest possible axis-aligned rectangle that uses any two red tiles as opposite corners. The area is calculated as the number of tiles inside the rectangle, including the boundary.

### Part 2

The rectangle must now only include tiles that are red or green. Green tiles are those that connect consecutive red tiles (forming the boundary) and all tiles inside the closed loop formed by the red and green tiles. The rectangle must still use two red tiles as opposite corners, but all other tiles within the rectangle must be red or green.

## 🧠 Solution Logic

The solution is implemented in **Python** and efficiently handles large coordinate values using coordinate compression and scanline techniques.

### Key Concepts

- **Brute-force Pairing:** For both parts, every pair of red tiles is considered as possible opposite corners of a rectangle.
- **Area Calculation:** The area is $(|x_2 - x_1| + 1) \times (|y_2 - y_1| + 1)$.
- **Efficient Validation:**
  - For Part 1, all rectangles are valid.
  - For Part 2, the solution builds a set of valid x-ranges for each critical y-band using the polygon's edges and interior, allowing fast validation of whether a rectangle is fully covered by red or green tiles.
- **Coordinate Compression:** Only critical y-values (where the polygon changes) are checked, making the solution efficient even for very large grids.

### Implementation

- **Input:** Each line in `input.txt` contains the $x, y$ coordinates of a red tile, separated by a comma.
- **Output:**
  - Part 1: The largest possible rectangle area using any two red tiles as opposite corners.
  - Part 2: The largest possible rectangle area using only red and green tiles.

#### Main Functions

- Parses the input and builds the polygon boundary.
- For Part 2, constructs y-bands and x-ranges for efficient rectangle validation.
- Iterates over all pairs of red tiles to find the largest valid rectangle.

## 🚀 How to Run

1. Place the puzzle input in `input.txt` (one coordinate per line, as `x,y`).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — The puzzle input with red tile coordinates.
