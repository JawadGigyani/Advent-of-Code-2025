# Advent of Code 2025 - Day 3: Lobby

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/3)

## 🏢 Problem Description

The lobby's escalator is offline and needs emergency power from battery banks. Each bank is a line of digits (1-9), each digit representing a battery's joltage rating.

### Part 1

For each bank, you must turn on **exactly two batteries** (pick two digits, in order, from the line). The joltage is the two digits, concatenated in order (e.g., picking positions 2 and 4 in `12345` gives `24`).

Find the largest possible joltage for each bank and sum them all.

### Part 2

Now, you must turn on **exactly twelve batteries** in each bank. The joltage is the 12-digit number formed by the selected digits, in order. Find the largest possible 12-digit number for each bank and sum them all.

## 🧠 Solution Logic

The solution is implemented in **Python** and efficiently finds the largest possible number for each bank.

### Key Concept: Lexicographically Largest Subsequence

- For Part 1: For each digit, pair it with the largest digit to its right.
- For Part 2: Use a greedy stack to build the largest 12-digit number by always keeping the best possible digits in order.

### Implementation

- **Input:** Each line in `input.txt` is a bank of digits.
- **Output:** The sum of the largest possible numbers (2-digit for Part 1, 12-digit for Part 2) from each bank.

#### Main Functions

- `max_joltage(bank)`: Finds the largest 2-digit number for Part 1.
- `max_joltage_12(bank)`: Finds the largest 12-digit number for Part 2 using a greedy stack.
- `main()`: Reads input, computes the total, and prints the result.

## 🚀 How to Run

1. Place puzzle input in `input.txt` (one bank per line).
2. Run the script:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Solution code for both parts.
- `input.txt` — Puzzle input.
