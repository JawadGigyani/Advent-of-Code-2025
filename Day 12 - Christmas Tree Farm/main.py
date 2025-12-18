from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, List, Sequence, Tuple


Coord = Tuple[int, int]


@dataclass(frozen=True)
class Shape:
    cells: Tuple[Coord, ...] 


@dataclass(frozen=True)
class Region:
    width: int
    height: int
    counts: Tuple[int, ...]


def _normalize_cells(cells: Sequence[Coord]) -> Tuple[Coord, ...]:
    min_x = min(x for x, _ in cells)
    min_y = min(y for _, y in cells)
    norm = sorted((x - min_x, y - min_y) for x, y in cells)
    return tuple(norm)


def _rotate90(cells: Sequence[Coord]) -> Tuple[Coord, ...]:
    rotated = [(y, -x) for x, y in cells]
    return _normalize_cells(rotated)


def _flip_h(cells: Sequence[Coord]) -> Tuple[Coord, ...]:
    flipped = [(-x, y) for x, y in cells]
    return _normalize_cells(flipped)


def all_orientations(shape: Shape) -> List[Shape]:
    seen = set()
    out: List[Shape] = []
    base = shape.cells
    cur = base
    for _ in range(4):
        cur = _normalize_cells(cur)
        if cur not in seen:
            seen.add(cur)
            out.append(Shape(cur))
        fh = _flip_h(cur)
        if fh not in seen:
            seen.add(fh)
            out.append(Shape(fh))
        cur = _rotate90(cur)
    return out


def shape_area(shape: Shape) -> int:
    return len(shape.cells)


def shape_bounds(shape: Shape) -> Tuple[int, int]:
    max_x = max(x for x, _ in shape.cells)
    max_y = max(y for _, y in shape.cells)
    return max_x + 1, max_y + 1


def parse_input(filename: str) -> tuple[List[Shape], List[Region]]:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    shapes: Dict[int, Shape] = {}
    regions: List[Region] = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        if line.endswith(":") and line[:-1].isdigit():
            shape_idx = int(line[:-1])
            i += 1
            cells: List[Coord] = []
            y = 0
            while i < len(lines):
                row = lines[i]
                if row == "":
                    break
                if row.strip().endswith(":") and row.strip()[:-1].isdigit():
                    break
                for x, ch in enumerate(row):
                    if ch == "#":
                        cells.append((x, y))
                y += 1
                i += 1
            if not cells:
                raise ValueError(f"Shape {shape_idx} has no occupied cells")
            shapes[shape_idx] = Shape(_normalize_cells(cells))
            continue

        if "x" in line and ":" in line and line[0].isdigit():
            size, rest = line.split(":", 1)
            w_str, h_str = size.split("x")
            w, h = int(w_str), int(h_str)
            counts = tuple(int(x) for x in rest.strip().split()) if rest.strip() else tuple()
            regions.append(Region(width=w, height=h, counts=counts))
            i += 1
            continue

        i += 1

    max_idx = max(shapes) if shapes else -1
    shape_list = [shapes[idx] for idx in range(max_idx + 1)]
    return shape_list, regions


def required_occupied_cells(shapes: Sequence[Shape], counts: Sequence[int]) -> int:
    total = 0
    for idx, cnt in enumerate(counts):
        if cnt:
            total += cnt * shape_area(shapes[idx])
    return total


def solve_region_exact(width: int, height: int, counts: Sequence[int], shape_orients: Sequence[List[Shape]]) -> bool:
    area = width * height

    pieces: List[int] = []
    for idx, cnt in enumerate(counts):
        pieces.extend([idx] * cnt)
    if not pieces:
        return True

    placements: List[List[int]] = [[] for _ in range(len(shape_orients))]
    for idx, orients in enumerate(shape_orients):
        for s in orients:
            sw, sh = shape_bounds(s)
            for y in range(height - sh + 1):
                for x in range(width - sw + 1):
                    mask = 0
                    for cx, cy in s.cells:
                        pos = (y + cy) * width + (x + cx)
                        mask |= 1 << pos
                    placements[idx].append(mask)

    pieces.sort(key=lambda idx: len(placements[idx]))

    @lru_cache(maxsize=None)
    def backtrack(i: int, used_mask: int) -> bool:
        if i == len(pieces):
            return True
        shape_idx = pieces[i]
        for pm in placements[shape_idx]:
            if pm & used_mask:
                continue
            if backtrack(i + 1, used_mask | pm):
                return True
        return False

    if area > 300:
        raise ValueError("Exact solver called on a region that is too large")

    return backtrack(0, 0)


def region_fits(width: int, height: int, counts: Sequence[int], shapes: Sequence[Shape], shape_orients: Sequence[List[Shape]]) -> bool:
    needed = required_occupied_cells(shapes, counts)
    if needed > width * height:
        return False

    if width * height <= 300 and sum(counts) <= 30:
        return solve_region_exact(width, height, counts, shape_orients)
    return True

def main():
    shapes, regions = parse_input("input.txt")
    shape_orients = [all_orientations(s) for s in shapes]
    ok = 0
    for r in regions:
        if region_fits(r.width, r.height, r.counts, shapes, shape_orients):
            ok += 1
    print(ok)

if __name__ == "__main__":
    main()