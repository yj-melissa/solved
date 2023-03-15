def dfs(graph, v, visited):
    global count
    # 방문처리
    visited[v] = 1
    # print(v, end=' ')
    count += 1

    for next in graph[v]:
        if visited[next] == 0:
            dfs(graph, next, visited)
    else:
        return

com_qty = int(input())          # 컴퓨터의 수
com_rel = int(input())          # 연결된 쌍의 수
graph = [[] for _ in range(com_qty + 1)]      # 컴퓨터 연결 관계 확인
for _ in range(com_rel):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)                # 양방향 연결
    graph[com2].append(com1)

visited = [0] * (com_qty + 1)
stack = []
count = -1                  # 1번 컴퓨터 제외
dfs(graph, 1, visited)
print(count)
