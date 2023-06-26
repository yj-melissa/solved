from collections import deque

def solution(priorities, location):
    answer = 0
    processes = [(i, priorities[i]) for i in range(len(priorities))]    # (원래idx, 우선순위)
    processes = deque(processes)
    
    while processes:
        idx, priority = processes.popleft()
        for i, p in processes:      # 큐 안에 남아있는 프로세스 검사
            if p > priority:        # 우선순위 더 높은 일이 있으면 검사 중단, 큐에 넣음
                processes.append((idx, priority))
                break
        else:           # 더 높은 우선순위가 없었을 때
            answer += 1
            if idx == location:
                return answer
    
    return answer