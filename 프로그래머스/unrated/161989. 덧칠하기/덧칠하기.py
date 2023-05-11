def solution(n, m, section):
    answer = 0
    e = 0       # 색칠한 구역
    
    for s in section:
        if s <= e :      # 이미 색칠한 구역이라면 패스
            continue
        
        answer += 1
        e = s + m - 1
    
    return answer