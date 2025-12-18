def parse_input(filename):
    with open(filename) as f:
        coords = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]
    return coords

def build_y_bands(coords):
    n = len(coords)
    
    v_segments = []
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        if x1 == x2:
            v_segments.append((x1, min(y1, y2), max(y1, y2)))
    
    h_segments = []
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        if y1 == y2:
            h_segments.append((y1, min(x1, x2), max(x1, x2)))
    
    all_ys = set()
    for x, y1, y2 in v_segments:
        all_ys.add(y1)
        all_ys.add(y2)
    all_ys = sorted(all_ys)
    
    def get_interior_x_ranges(y):
        crossings = []
        for x, y1, y2 in v_segments:
            if y1 < y < y2:
                crossings.append(x)
        crossings.sort()
        
        ranges = []
        for i in range(0, len(crossings) - 1, 2):
            ranges.append((crossings[i], crossings[i + 1]))
        return ranges
    
    def get_boundary_x_ranges(y):
        ranges = []

        for hy, hx1, hx2 in h_segments:
            if hy == y:
                ranges.append((hx1, hx2))
        
        for x, y1, y2 in v_segments:
            if y1 <= y <= y2:
                ranges.append((x, x))
        
        interior_above = get_interior_x_ranges(y + 0.5)
        interior_below = get_interior_x_ranges(y - 0.5)
        ranges.extend(interior_above)
        ranges.extend(interior_below)
        
        if not ranges:
            return []
        ranges.sort()
        merged = [list(ranges[0])]
        for r in ranges[1:]:
            if r[0] <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], r[1])
            else:
                merged.append(list(r))
        return [tuple(r) for r in merged]
    
    bands = []
    for i, y in enumerate(all_ys):
        x_ranges = get_boundary_x_ranges(y)
        if x_ranges:
            bands.append((y, y, x_ranges))

        if i + 1 < len(all_ys):
            next_y = all_ys[i + 1]
            if next_y > y + 1:
                mid_y = (y + next_y) / 2.0
                interior_ranges = get_interior_x_ranges(mid_y)
                if interior_ranges:
                    bands.append((y + 1, next_y - 1, interior_ranges))
    
    return bands

def is_rectangle_valid_fast(y1, y2, x1, x2, bands):
    min_y, max_y = min(y1, y2), max(y1, y2)
    min_x, max_x = min(x1, x2), max(x1, x2)
    
    covered_y = min_y
    for y_start, y_end, x_ranges in bands:
        if y_end < min_y:
            continue
        if y_start > max_y:
            break
        
        if y_start > covered_y:
            return False
        
        x_covered = False
        for rx1, rx2 in x_ranges:
            if rx1 <= min_x and max_x <= rx2:
                x_covered = True
                break
        
        if not x_covered:
            return False
        
        covered_y = max(covered_y, y_end + 1)
    
    return covered_y > max_y

def largest_rectangle_part1(coords):
    """Part 1: Largest rectangle with any two red corners."""
    max_area = 0
    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i + 1, n):
            x2, y2 = coords[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area
    return max_area

def largest_rectangle_part2(coords):
    """Part 2: Largest rectangle using only red and green tiles."""
    bands = build_y_bands(coords)
    
    max_area = 0
    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i + 1, n):
            x2, y2 = coords[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area and is_rectangle_valid_fast(y1, y2, x1, x2, bands):
                max_area = area
    return max_area

def main():
    coords = parse_input("input.txt")
    print("Part 1:", largest_rectangle_part1(coords))
    print("Part 2:", largest_rectangle_part2(coords))

if __name__ == "__main__":
    main()