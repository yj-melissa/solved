def solution(N, stages):            # N = 전체 스테이지 개수, stages = 사용자가 멈춰있는 스테이지 번호
    stage_users = [stages.count(x) for x in range(N+2)]     # 각 스테이지에 멈춰있는 사용자 수
    fail_rate = []         # 실패율 목록
    cleared_users = stage_users[N+1]               # 윗 스테이지에 있는 유저의 수
    
    # 1. N+1 -> 1스테이지 순으로 탐색
    for i in range(N, 0, -1):
        
        # 2. 실패율 = 현재 스테이지에 있는 유저 수 / 클리어한 유저 수 + 현재 스테이지에 있는 유저 수
        if stage_users[i] > 0:
            percent = stage_users[i] / (cleared_users + stage_users[i])
        else:
            percent = 0
            
        fail_rate.append((i, percent))
        
        # 3. cleared_users += stage_users[i]
        cleared_users += stage_users[i]
    
    # 4. 실패율 높은 순으로 정렬 (실패율 내림차순, 실패율 같은 경우 오름차순)
    fail_rate.sort(key = lambda x : (-x[1], x[0]))
    
    # 5. answer에 추가
    answer = [f[0] for f in fail_rate]    
    
    return answer