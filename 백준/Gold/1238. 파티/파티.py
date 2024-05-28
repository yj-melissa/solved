import heapq

def dijkstra(s, N):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for next, c in graph[now]:
            new_cost = c + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(q, (new_cost, next))

    return distance


INF = int(1e9)

N, M, X = map(int, input().split())     # N : 마을, M : 도로 수, X : 목적지
graph = [[] for _ in range(N + 1)]
total_time = [0] * (N + 1)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

for i in range(1, N + 1):
    total_time[i] += dijkstra(i, N)[X]       # 집 -> X
    total_time[i] += dijkstra(X, N)[i]       # X -> 집

print(max(total_time))