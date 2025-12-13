from functools import lru_cache

def read_grid(filename):
    with open(filename) as f:
        grid = [line.rstrip('\n') for line in f if line.strip()]
    return grid

def find_start(grid):
    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            return r, c
    raise ValueError("No starting point 'S' found.")

def count_timelines(grid):
    rows, cols = len(grid), len(grid[0])
    start_r, start_c = find_start(grid)

    @lru_cache(maxsize=None)
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return 1 
        cell = grid[r][c]
        if cell == '.':
            return dfs(r + 1, c)
        elif cell == '^':
            left = dfs(r + 1, c - 1) if c - 1 >= 0 else 1
            right = dfs(r + 1, c + 1) if c + 1 < cols else 1
            return left + right
        else:
            return 0 

    return dfs(start_r + 1, start_c)

def main():
    grid = read_grid("input.txt")
    print(count_timelines(grid))

if __name__ == "__main__":
    main()