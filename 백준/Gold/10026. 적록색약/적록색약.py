def is_in_range(row, col):
    global N
    if (0 <= row < N) and (0 <= col < N):
        return True
    else:
        return False

def is_not_visited(row, col):
    if visited[row][col] == 0:
        return True
    else:
        return False

def dfs(i, j, color):
    stack = []
    delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    visited[i][j] = 1
    stack.append((i, j, color))

    while stack:
        row, col, c = stack.pop()

        for dr, dc in delta:
            nr, nc = row + dr, col + dc

            if is_in_range(nr, nc) and is_not_visited(nr, nc) and graph[nr][nc] == color:
                visited[nr][nc] = 1
                stack.append((nr, nc, graph[nr][nc]))


N = int(input())
graph = []

for _ in range(N):
    graph.append(list(input()))

visited = [[0] * N for _ in range(N)]

# 색약 아닌 경우
not_weakness = 0

for i in range(N):
    for j in range(N):
        if is_not_visited(i, j):
            dfs(i, j, graph[i][j])
            not_weakness += 1

# visited 초기화, R -> G 변경
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 색약인 경우
weakness = 0
for i in range(N):
    for j in range(N):
        if is_not_visited(i, j):
            dfs(i, j, graph[i][j])
            weakness += 1

print(not_weakness, weakness)