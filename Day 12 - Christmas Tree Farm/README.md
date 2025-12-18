# Advent of Code 2025 - Day 12: Christmas Tree Farm

[View the full puzzle on Advent of Code](https://adventofcode.com/2025/day/12)

## 🎄 Problem Description

In the Christmas Tree Farm cavern, the protagonist must determine whether each tree’s rectangular region can fit a specified multiset of presents.

The input has two sections:

1. **Present shapes** (indexed): each shape is drawn on a unit grid with `#` for occupied cells and `.` for empty cells.

2. **Regions**: each line describes a rectangle `WxH` and the number of presents required of each shape index.

Presents may be rotated and flipped, must align to the grid, and may not overlap on occupied (`#`) cells.

The goal is to count how many regions can fit all required presents.

## 🧠 Solution Logic

This problem is a **grid packing** (polyomino-like) feasibility check:

- Each present occupies the `#` cells of its shape.
- Shapes may be rotated/flipped.
- Presents must not overlap on occupied cells.

In general, exact packing is NP-hard. The key to solving it in practice is to use an exact solver where it’s feasible, and a very fast necessary-condition filter for large cases.

### Strategy Used Here

The implementation uses a hybrid approach:

1. **Always apply the necessary area check**

Let:

$$needed = \sum_i (count_i \times area(shape_i))$$
$$capacity = W \times H$$

If `needed > capacity`, the region cannot fit the presents.

2. **Exact solver for small regions (matches the statement examples)**

For small boards and small present counts, the code runs an exact bitmask backtracking solver:

- Precomputes every valid placement (as a bitmask) for each shape orientation.
- Uses a memoized DFS that tries to place presents with the fewest placement options first.

This correctly handles the official examples where geometry (not just area) matters.

3. **Fast shortcut for very large regions**

For large regions with hundreds of presents, an exact solver is not computationally practical. In that regime, the code falls back to the area condition as the only scalable filter.

If full, always-correct packing is required for large regions, the solver would need a fundamentally different technique (e.g., specialized constructive packing guarantees for the specific shape set).

## 🚀 How to Run

1. Put the puzzle input in `input.txt`.
2. Run:
   ```bash
   python main.py
   ```

## 📦 Files

- `main.py` — Parses shapes/regions and counts feasible regions.
- `input.txt` — Puzzle input.
