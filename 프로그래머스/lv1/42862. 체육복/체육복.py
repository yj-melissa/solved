def solution(n, lost, reserve):
    answer = [1] * (n + 1)      # 체육복 현황
    
    for i in range(1, n+1):
        if i in reserve:        # 체육복 여분 있는 경우
            answer[i] += 1
        
        if i in lost:           # 체육복 도난 당한 경우
            answer[i] -= 1
            
        if answer[i] == 1:
            continue
        
        if answer[i] == 0:
            if answer[i-1] == 2:        # 앞 사람이 체육복 여벌 있으면 빌림
                answer[i] += 1
                continue
        
        if answer[i] == 2:
            if answer[i-1] == 0:
                answer[i-1] += 1
                answer[i] -= 1
    
    return n - answer.count(0)