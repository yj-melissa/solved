import heapq

def solution(scoville, K):
    answer = 0
    h = []
    
    # heap에 스코빌 지수 추가
    for s in scoville:
        heapq.heappush(h, s)
    
    # 음식 섞기
    while True:
        f = heapq.heappop(h)
        
        if f >= K:       # 스코빌 제일 낮은 음식이 K 넘음
            break
        
        if len(h) == 0:     # 더이상 섞을 음식 없음
            answer = -1
            break
            
        s = heapq.heappop(h)
        
        new = f + (s * 2)
        heapq.heappush(h, new)
        answer += 1
        
        
        
    return answer