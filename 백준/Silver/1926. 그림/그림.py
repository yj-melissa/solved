import sys
sys.setrecursionlimit(10**7)

def is_visited(row, col):
    if visited[row][col] == 1:
        return True
    else:
        return False

def is_in_range(row, col):
    global N, M
    if 0 <= row < N and 0 <= col < M:
        return True
    else:
        return False

def dfs(row, col, area):
    if is_visited(row, col):
        return area
    else:
        visited[row][col] = 1       # 방문처리

    if info[row][col] == 0:
        return area

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상

    for dr, dc in delta:
        nr = row + dr
        nc = col + dc

        if not is_in_range(nr, nc):
            continue

        area = dfs(nr, nc, area)

    return area + 1


N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0         # 그림의 개수
max_area = 0    # 가장 넓은 넓이

for row in range(N):
    for col in range(M):
        if not is_visited(row, col) and info[row][col] == 1:
            cnt += 1
            area = dfs(row, col, 0)
            if area > max_area:
                max_area = area

print(cnt, max_area)