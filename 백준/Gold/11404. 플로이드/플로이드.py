INF = int(1e9)

n = int(input())        # 도시 개수
m = int(input())        # 버스 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):          # 버스 노선 정보 입력
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):       # 시착 = 도착인 경우 비용 0
    graph[i][i] = 0

for k in range(1, n + 1):       # 플로이드 : i -> j, i -> k -> j 비용 비교
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end = ' ')
    print()