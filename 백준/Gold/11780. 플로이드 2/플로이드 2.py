INF = int(1e9)

n = int(input())        # 도시 개수
m = int(input())        # 버스 개수
graph = [[INF] * (n + 1) for _ in range(n + 1)]
path = [[list()] * (n + 1) for i in range(n + 1)]         # 경로 저장


for i in range(1, n + 1):
    graph[i][i] = 0     # 자기 자신으로 가는 비용은 0

for _ in range(m):      # 버스 정보 입력
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
        path[a][b] = [a, b]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_cost = graph[i][k] + graph[k][j]
            if new_cost < graph[i][j]:
                graph[i][j] = new_cost
                path[i][j] = path[i][k][:-1] + path[k][j]

for i in range(1, n + 1):               # 최소 비용 출력
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end = ' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if len(path[i][j]) == 0:
            print(0)
        else:
            print(len(path[i][j]), end = ' ')
            for p in path[i][j]:
                print(p, end = ' ')
            print()