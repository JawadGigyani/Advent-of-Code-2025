from __future__ import annotations

from collections import defaultdict, deque
import sys
from typing import DefaultDict, Dict, Iterable, List, Set, Tuple


Graph = Dict[str, List[str]]


def parse_input(filename: str) -> Graph:
    graph: DefaultDict[str, List[str]] = defaultdict(list)
    nodes: Set[str] = set()

    with open(filename, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if ":" not in line:
                continue
            src, rest = line.split(":", 1)
            src = src.strip()
            targets = rest.strip().split() if rest.strip() else []
            graph[src].extend(targets)
            nodes.add(src)
            nodes.update(targets)

    for node in nodes:
        graph.setdefault(node, [])

    return dict(graph)


def nodes_that_can_reach(graph: Graph, end: str) -> Set[str]:
    rev: DefaultDict[str, List[str]] = defaultdict(list)
    for src, dsts in graph.items():
        for dst in dsts:
            rev[dst].append(src)

    seen: Set[str] = set()
    q: deque[str] = deque([end])
    seen.add(end)
    while q:
        cur = q.popleft()
        for prev in rev.get(cur, []):
            if prev not in seen:
                seen.add(prev)
                q.append(prev)
    return seen


def assert_no_cycle_on_relevant_paths(graph: Graph, start: str, end: str) -> None:
    can_reach_end = nodes_that_can_reach(graph, end)
    if start not in can_reach_end:
        return

    color: Dict[str, int] = {}  

    def dfs(u: str) -> None:
        color[u] = 1
        for v in graph.get(u, []):
            if v not in can_reach_end:
                continue
            c = color.get(v, 0)
            if c == 1:
                raise ValueError("Cycle detected on a path that can reach 'out'")
            if c == 0:
                dfs(v)
        color[u] = 2

    dfs(start)


def count_paths_part1(graph: Graph, start: str = "you", end: str = "out") -> int:
    can_reach_end = nodes_that_can_reach(graph, end)
    if start not in can_reach_end:
        return 0

    assert_no_cycle_on_relevant_paths(graph, start, end)

    sys.setrecursionlimit(1_000_000)
    memo: Dict[str, int] = {}

    def dfs(node: str) -> int:
        if node == end:
            return 1
        if node in memo:
            return memo[node]
        total = 0
        for nxt in graph.get(node, []):
            if nxt in can_reach_end:
                total += dfs(nxt)
        memo[node] = total
        return total

    return dfs(start)


def count_paths_part2(
    graph: Graph,
    start: str = "svr",
    end: str = "out",
    must_visit: Tuple[str, str] = ("dac", "fft"),
) -> int:
    can_reach_end = nodes_that_can_reach(graph, end)
    if start not in can_reach_end:
        return 0

    assert_no_cycle_on_relevant_paths(graph, start, end)

    a, b = must_visit
    bit_a = 1
    bit_b = 2

    def node_bits(node: str) -> int:
        bits = 0
        if node == a:
            bits |= bit_a
        if node == b:
            bits |= bit_b
        return bits

    sys.setrecursionlimit(1_000_000)
    memo: Dict[Tuple[str, int], int] = {}

    def dfs(node: str, mask: int) -> int:
        mask |= node_bits(node)
        key = (node, mask)
        if key in memo:
            return memo[key]
        if node == end:
            return 1 if mask == 3 else 0

        total = 0
        for nxt in graph.get(node, []):
            if nxt in can_reach_end:
                total += dfs(nxt, mask)
        memo[key] = total
        return total

    return dfs(start, 0)


def main() -> None:
    graph = parse_input("input.txt")
    print("Part 1:", count_paths_part1(graph))
    print("Part 2:", count_paths_part2(graph))


if __name__ == "__main__":
    main()