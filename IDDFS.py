def is_valid(r, c, grid, visited):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and not visited[r][c]
def dls(node, target, depth, grid, visited, path, traversal):
    (r, c) = node 
    visited[r][c] = True
    traversal.append((r, c))
    if node == target:
        path.append(node)
        return True
    if depth == 0:
        return False
    directions = [(-1, 0),(1, 0),(0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc, grid, visited):
           if dls((nr, nc), target, depth - 1, grid, visited, path, traversal):
              path.append(node)
              return True
    return False
def iddfs(star, target, grid):
    max_depth = len(grid) * len(grid[0])
    for depth in range(max_depth + 1):
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        path, traversal = [], []
        if dls(star, target, depth, grid, visited, path, traversal):
            path.reverse()
            return True, depth, traversal, path
    return False, max_depth, [], []
            
if __name__ == "__main__":
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(list(map(int, input().split())))
    sr, sc = map(int, input().split())
    tr, tc = map(int, input().split())
    start = (sr, sc)
    target = (tr, tc)
    found, depth, traversal, path = iddfs(start, target, grid)
    if found:
        print(f"Path found at depth {depth} using IDDFS")
        print(f"Traversal Order: {tuple(traversal)}")
        print(f"Path: {path}")
    else:
        print(f"Path not found at max depth {depth} using IDDFS")