def solution(progresses, speeds):
    answer = []
    len_progresses = len(progresses)
    released = [0] * len_progresses
    
    for i in range(len_progresses):
        days = (100 - progresses[i]) // speeds[i]           # 진행률 100%까지 필요한 날짜
        if (100 - progresses[i]) % speeds[i]:
            days += 1
        released[i] += days
    
    early = released[0]
    cnt = 0
    for j in range(len_progresses):
        late = released[j]
        if early >= late:       # 앞 기능 배포 날짜가 더 많거나 같다면 cnt += 1
            cnt += 1
            continue
        answer.append(cnt)          # 아니라면 answer에 cnt 추가
        early = late
        cnt = 1
    answer.append(cnt)
    
        
    return answer