import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    q = []
    result[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        distance, now = heapq.heappop(q)

        if result[now] < distance:
            continue

        for next, cost in graph[now]:
            new_distance = distance + cost
            if new_distance < result[next]:
                result[next] = new_distance
                heapq.heappush(q, (new_distance, next))


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = int(1e9)
result = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])