from collections import deque

def bfs(r, c, maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((r, c))
    
    maps[n - 1][m - 1] = -1
    
    while q:
        cr, cc = q.popleft()
        
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            # 범위 검사
            if (nr < 0) or (nr >= n) or (nc < 0) or (nc >= m):      
                continue
            
            # 벽 통과
            if maps[nr][nc] == 0:
                continue
                
            if (nr == n - 1) and (nc == m - 1):
                return maps[cr][cc] + 1
                
            if maps[nr][nc] == 1:
                maps[nr][nc] = maps[cr][cc] + 1
                q.append((nr, nc))
                
    return maps[n-1][m-1]
            
            
    
    
def solution(maps):
    return bfs(0, 0, maps)