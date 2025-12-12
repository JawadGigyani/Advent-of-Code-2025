import numpy as np
from scipy.signal import convolve2d

def main():
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    arr = np.array([[1 if c == '@' else 0 for c in row] for row in grid], dtype=int)

    # 3x3 kernel with center zero
    kernel = np.ones((3, 3), dtype=int)
    kernel[1, 1] = 0

    total_removed = 0
    while True:
        neighbor_counts = convolve2d(arr, kernel, mode='same', boundary='fill', fillvalue=0)
        accessible = (arr == 1) & (neighbor_counts < 4)
        removed_this_round = np.sum(accessible)
        if removed_this_round == 0:
            break
        arr[accessible] = 0
        total_removed += removed_this_round

    print(total_removed)

if __name__ == "__main__":
    main()