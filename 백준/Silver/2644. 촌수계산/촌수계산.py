def dfs(start, end, count):
    global answer
    # 방문 체크
    visited[start] = 1
    count += 1
    #print(start, count)

    # 도착점 체크
    if start == end:
        answer = count
        return

    # 다음 방문지 확인
    for nxt in people[start]:
        if visited[end] == 1:
            return
        if visited[nxt] == 0:
            dfs(nxt, end, count)



n = int(input())
frm, to = map(int, input().split())
m = int(input())
people = [[] for _ in range(n+1)]       # 관계도
for _ in range(m):
    p, c = map(int, input().split())        # 부모 - 자식
    people[p].append(c)
    people[c].append(p)

visited = [0] * (n+1)
answer = -1               # 촌수 체크
dfs(frm, to, -1)
print(answer)