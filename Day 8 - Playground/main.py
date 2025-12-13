import math
from collections import Counter

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False 
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def parse_input(filename):
    with open(filename) as f:
        points = []
        for line in f:
            line = line.strip()
            if line:
                x, y, z = map(int, line.split(','))
                points.append((x, y, z))
    return points

def main():
    points = parse_input("input.txt")
    n = len(points)

    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            pairs.append((dist, i, j))

    pairs.sort()

    uf = UnionFind(n)

    last_i, last_j = -1, -1
    circuits_remaining = n

    for dist, i, j in pairs:
        if uf.union(i, j):
            last_i, last_j = i, j
            circuits_remaining -= 1
            if circuits_remaining == 1:
                break

    result = points[last_i][0] * points[last_j][0]
    print(result)

if __name__ == "__main__":
    main()
