# Advent of Code 2025 - Day 8: Playground

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/8)

## 🕹️ Problem Description

In the Playground, the protagonist is tasked with connecting a set of 3D junction boxes using the shortest possible connections. Each box is defined by its $(x, y, z)$ coordinates. The challenge is to connect the boxes in a way that forms circuits, following specific rules for each part.

### Part 1

The program must connect the boxes by selecting the $n$ shortest possible connections (where $n$ is the number of boxes). After these connections, the sizes of all resulting circuits are determined, and the product of the sizes of the three largest circuits is calculated.

### Part 2

The task is to continue connecting boxes using the next shortest available connections until all boxes are part of a single circuit. The answer is the product of the $x$-coordinates of the last two boxes connected to form the final single circuit.

## 🧠 Solution Logic

The solution is implemented in **Python** and leverages efficient algorithms for managing connections and circuits.

### Key Concept: Union-Find and Pairwise Distance

- All pairwise Euclidean distances between boxes are calculated and sorted.
- A Union-Find (Disjoint Set Union) data structure is used to efficiently track and merge circuits as connections are made.
- For Part 1, the first $n$ shortest connections are processed, and the sizes of all resulting circuits are determined.
- For Part 2, connections continue until only one circuit remains, and the last successful connection is tracked.

### Implementation

- **Input:** Each line in `input.txt` contains the $x, y, z$ coordinates of a junction box, separated by commas.
- **Output:**
  - Part 1: The product of the sizes of the three largest circuits after $n$ connections.
  - Part 2: The product of the $x$-coordinates of the last two boxes connected to form a single circuit.

#### Main Functions

- Calculates all pairwise distances and sorts them.
- Uses Union-Find to merge circuits and track connections.
- For Part 2, tracks the last two boxes connected to form the final circuit.

## 🚀 How to Run

1. Place the puzzle input in `input.txt` (one box per line, as `x,y,z`).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — The puzzle input with 3D coordinates.
