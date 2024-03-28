from collections import deque

def is_visited(row, col):
    if visited[row][col] == 1:
        return True
    else:
        return False

def is_blank(row, col):
    if paper[row][col] == 0:
        return True
    else:
        return False

def is_out_of_range(row, col):
    global N, M
    if (0 <= row < N) and (0 <= col < M):
        return False
    else:
        return True

def bfs(row, col, area):
    global max_area
    queue = deque()
    queue.append((row, col))

    visited[row][col] = 1       # 방문 처리

    while queue:
        cr, cc = queue.popleft()
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc

            if is_out_of_range(nr, nc):
                continue

            if is_visited(nr, nc):
                continue

            if is_blank(nr, nc):
                continue

            queue.append((nr, nc))
            visited[nr][nc] = 1
            area += 1

    return area


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
max_area = 0

for row in range(N):
    for col in range(M):
        if is_visited(row, col) or is_blank(row, col):
            continue
        cnt += 1
        area = bfs(row, col, 1)
        if area > max_area:
            max_area = area

print(cnt, max_area)