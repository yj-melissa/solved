def solution(citations):
    answer = 0
    max_citations = max(citations)          # 최대 인용 횟수
    h_list = [0] * max_citations            # h번 이상 인용된 논문의 편수
    
    for c in citations:
        for h in range(c):      # 논문 횟수 더해줌
            h_list[h] += 1
            
    for i in range(max_citations-1, 0, -1):     # H-Index 확인
        if h_list[i] >= (i+1):
            answer = i+1
            break    
    
    return answer