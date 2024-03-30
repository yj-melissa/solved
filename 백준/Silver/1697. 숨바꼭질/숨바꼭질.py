from collections import deque

def bfs(start):
    global K
    visited[start] = 0
    queue.append(start)

    while queue:
        now = queue.popleft()
        possible = [now + 1, now - 1, now * 2]
        for next in possible:
            if 0 <= next <= 100000:
                if visited[next] > -1:
                    continue
                visited[next] = visited[now] + 1
                queue.append(next)
                if next == K:
                    return


N, K = map(int, input().split())
queue = deque()
visited = [-1] * (100001)

bfs(N)

print(visited[K])