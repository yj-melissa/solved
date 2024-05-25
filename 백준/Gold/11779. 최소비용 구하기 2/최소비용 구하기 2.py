import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    h = []
    heapq.heappush(h, (0, start))

    while h:
        cost, now = heapq.heappop(h)
        if costs[now] < cost:
            continue

        for next, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < costs[next]:
                costs[next] = new_cost
                parents[next] = now
                heapq.heappush(h, (new_cost, next))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
S, E = map(int, input().split())
costs = [INF] * (n + 1)
parents = [0] * (n + 1)

dijkstra(S, E)


path = [str(E)]
now = E
while now != S:
    now = parents[now]
    path.append(str(now))
path.reverse()

print(costs[E])
print(len(path))
print(" ".join(path))
