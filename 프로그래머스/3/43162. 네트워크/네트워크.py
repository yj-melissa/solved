def solution(n, computers):
    answer = 0
    visited = [0] * n
    stack = []
    
    for i in range(n):
        if visited[i] == 1:     # 방문한 컴퓨터라면 넘어감
            continue
        
        visited[i] = 1         # 시작 컴퓨터 방문처리
        answer += 1
        stack.append(i)
        
        while stack:            # 연결 네트워크 탐색
            s = stack.pop()
            visited[s] = 1
            
            for j in range(n):
                if visited[j] == 1:
                    continue
                if computers[s][j] == 1:
                    stack.append(j)             
    
    return answer