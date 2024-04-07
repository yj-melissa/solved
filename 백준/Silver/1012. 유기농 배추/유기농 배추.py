def dfs():
    answer = 0
    visited = [[0] * M for _ in range(N)]
    stack = []

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for row in range(N):
        for col in range(M):
            if farm[row][col] == 1 and visited[row][col] == 0:
                stack.append((row, col))
                answer += 1

            while stack:
                cr, cc = stack.pop()
                if visited[cr][cc] == 1:
                    continue
                visited[cr][cc] = 1       # 방문처리

                for dr, dc in delta:        # 다음 칸 이동
                    nr = cr + dr
                    nc = cc + dc

                    if (0 <= nr < N) and (0 <= nc < M) and (farm[nr][nc] == 1):
                        stack.append((nr, nc))

    return answer


T = int(input())
for _ in range(T):
    # 배추 위치 입력
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    print(dfs())