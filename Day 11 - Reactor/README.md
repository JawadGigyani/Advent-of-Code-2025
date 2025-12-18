# Advent of Code 2025 - Day 11: Reactor

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/11)

## ⚡ Problem Description

Deep beneath the factory, the protagonist encounters a toroidal reactor and a tangle of devices connected by cables. Each device is described by a line of the form:

```
device: out1 out2 out3
```

This means `device` forwards data to each listed output device. Data flows only in the direction of these connections.

### Part 1

The task is to count all distinct paths that data can take from the device labeled `you` to the device labeled `out`.

### Part 2

The Elves discover that the problematic data path must pass through both `dac` and `fft` (in any order). Now, the task is to count all paths from `svr` to `out` that visit both `dac` and `fft` at least once.

## 🧠 Solution Logic

The solution is implemented in **Python** and models the device network as a directed graph.

### Key Concepts

- **Directed Graph Traversal:** Each device and its outputs form a node and directed edges.
- **Path Counting with Constraints:**
  - For Part 1, count all paths from `you` to `out`.
  - For Part 2, count all paths from `svr` to `out` that visit both `dac` and `fft`.
- **Memoized DFS (Dynamic Programming):**
  - For Part 1, memoize the number of paths from each node to `out`.
  - For Part 2, memoize the number of paths from each node to `out` for each possible combination of having visited `dac` and/or `fft`.
- **Cycle Detection:** The code checks for cycles on relevant paths to ensure the number of paths is finite.

### Implementation

- **Input:** Each line in `input.txt` describes a device and its outputs.
- **Output:**
  - Part 1: The number of distinct paths from `you` to `out`.
  - Part 2: The number of distinct paths from `svr` to `out` that visit both `dac` and `fft`.

#### Main Functions

- Parses the input and builds the directed graph.
- Uses memoized DFS to efficiently count paths.
- For Part 2, tracks which required devices have been visited using a bitmask.

## 🚀 How to Run

1. Place the puzzle input in `input.txt` (one device per line).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — The puzzle input describing the device network.

## 📝 Example

Given the following device list:

```
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
```

- **Part 1:** There are 8 distinct paths from `svr` to `out`.
- **Part 2:** Only 2 of those paths visit both `dac` and `fft`.

## 🧩 Results

- On the provided input:
  - Part 1: `599`
  - Part 2: `393474305030400`
