# Advent of Code 2025 - Day 7: Laboratories

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/7)

## 🧪 Problem Description

In the Laboratories, the protagonist encounters a teleporter manifold puzzle. A tachyon beam enters the manifold at the location marked `S` and always moves downward. The grid contains empty spaces (`.`) and splitters (`^`). When a beam encounters a splitter, it stops and two new beams are created: one to the left and one to the right, both continuing downward. The task is to analyze the manifold and count the number of times the beam is split.

### Part 1

The program simulates the path of the beam, counting each time it is split by a splitter. The simulation continues until all beams either exit the grid or hit a splitter.

### Part 2

The puzzle introduces a quantum twist: a single tachyon particle takes every possible path through the manifold, splitting at every splitter. The goal is to count the total number of unique timelines (paths) the particle can take through the manifold, using the many-worlds interpretation.

## 🧠 Solution Logic

The solution is implemented in **Python** and efficiently simulates the beam's journey through the manifold.

### Key Concept: Beam Simulation and Path Counting

- For Part 1, a BFS/queue simulation is used to track all active beams and count splits.
- For Part 2, a recursive DFS with memoization counts all possible timelines, splitting at each splitter and summing the results.

### Implementation

- **Input:** Each line in `input.txt` is a row of the manifold grid.
- **Output:**
  - Part 1: The number of times the beam is split.
  - Part 2: The total number of unique timelines (paths) through the manifold.

#### Main Functions

- Simulates the beam's movement and splitting using BFS for Part 1.
- Uses recursive DFS with memoization to count all possible timelines for Part 2.

## 🚀 How to Run

1. Place the puzzle input in `input.txt` (one grid row per line).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — The puzzle input grid.
