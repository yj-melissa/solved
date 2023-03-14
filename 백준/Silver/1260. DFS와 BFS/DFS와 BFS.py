from collections import deque

def dfs(v):
    # 방문 처리
    visited[v] = 1
    dfs_answer.append(v)

    graph[v].sort()     # 정점 번호가 작은 것 먼저 방문
    # 현재 정점에서 갈 수 있는 정점 확인
    for next in graph[v]:
        if visited[next] == 0:
            dfs(next)

def bfs(v):
    # 방문처리
    visited[v] = 1
    bfs_answer.append(v)
    queue.append(v)
    while queue:
        next = queue.popleft()
        graph[next].sort()
        for i in graph[next]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                bfs_answer.append(i)


# 입력
n, m, v = map(int, input().split())     # 정점 개수, 간선 개수, 시작 정점
graph = [[] for _ in range(n+1)]
for _ in range(m):
    frm, to = map(int, input().split())
    graph[frm].append(to)
    graph[to].append(frm)           # 양방향 간선

# dfs
visited = [0] * (n+1)
dfs_answer = []
dfs(v)
print(*dfs_answer)

# bfs
queue = deque()
bfs_answer = []
visited = [0] * (n+1)               # visited 초기화
bfs(v)
print(*bfs_answer)

