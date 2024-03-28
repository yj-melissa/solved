from collections import deque

def bfs(row, col):
    global N, M
    queue = deque()
    queue.append((row, col))

    while queue:
        cr, cc = queue.popleft()
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]      # 우하좌상
        for dr, dc in delta:
            nr, nc = cr + dr, cc + dc

            if not (0 <= nr < N) or not (0 <= nc < M):  # 범위 체크
                continue

            if maps[nr][nc] == 1:       # 이동 가능 + 아직 방문 x
                queue.append((nr, nc))
                maps[nr][nc] = maps[cr][cc] + 1

    return maps[N - 1][M - 1]


N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

answer = bfs(0, 0)

print(answer)