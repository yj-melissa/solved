from collections import deque

def bfs():
    while queue:
        cr, cc = queue.popleft()
        for dr, dc in delta:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if box[nr][nc] == 0:
                box[nr][nc] = box[cr][cc] + 1
                queue.append((nr, nc))


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]      # 왼오앞뒤 순
queue = deque()

for row in range(N):                # 시작부터 익어 있는 토마토 확인
    for col in range(M):
        if box[row][col] == 1:
            queue.append((row, col))

bfs()

answer = 0
for row in box:
    if 0 in row:          # 토마토가 모두 익지 못하는 상황
        answer = -1
        break
    answer = max(answer, max(row) - 1)

print(answer)
