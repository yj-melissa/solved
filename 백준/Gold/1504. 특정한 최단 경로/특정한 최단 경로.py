import heapq
import sys
input = sys.stdin.readline

def dijkstra(s, N):
    INF = int(1e9)
    distance = [INF] * (N + 1)
    q = []

    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, d in graph[now]:
            new_dist = d + dist
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(q, (new_dist, next))

    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):          # 양방향 길 추가
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


distance_from_1 = dijkstra(1, N)
distance_from_v1 = dijkstra(v1, N)
distance_from_v2 = dijkstra(v2, N)

dist1 = distance_from_1[v1] + distance_from_v1[v2] + distance_from_v2[N]
dist2 = distance_from_1[v2] + distance_from_v2[v1] + distance_from_v1[N]

answer = min(dist1, dist2) if ((dist1 < int(1e9)) and (dist2 < int(1e9))) else -1

print(answer)