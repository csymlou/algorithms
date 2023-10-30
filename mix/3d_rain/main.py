import heapq

q = []
wall = {}

height_map = [
    [3, 3, 3, 3, 3],
    [3, 2, 2, 2, 3],
    [3, 2, 1, 2, 3],
    [3, 2, 2, 2, 3],
    [3, 3, 3, 3, 3],
]
rows, cols = len(height_map), len(height_map[0])
if rows <= 2 or cols <= 2:
    exit(0)
total, cnt = rows * cols, 0
result = 0
for r in [0, rows - 1]:
    for j in range(cols):
        heapq.heappush(q, (height_map[r][j], r, j))
        cnt += 1
        wall[(r, j)] = 1
for c in [0, cols - 1]:
    for i in range(1, rows - 1):
        heapq.heappush(q, (height_map[i][c], i, c))
        cnt += 1
        wall[(i, c)] = 1

while cnt < total:
    h, i, j = heapq.heappop(q)
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x = i + dx
        y = j + dy
        if 0 <= x < rows and 0 <= y < cols and (x, y) not in wall:
            t = height_map[x][y]
            if h > t:
                result += h - t
            heapq.heappush(q, (max(h, t), x, y))
            cnt += 1
            wall[(x, y)] = 1

print(result)
