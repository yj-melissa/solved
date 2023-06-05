def solution(k, tangerine):  
    answer = 0
    
    sizes = dict()
    for s in tangerine:
        if s in sizes:
            sizes[s] += 1
        else:
            sizes[s] = 1
    
    sizes = list(sorted(sizes.items(), key = lambda x: x[1], reverse = True))
    
    total = 0          # 귤의 개수
    
    for _, c in sizes:
        total += c 
        answer += 1
        if total >= k:
            return answer
    
            
    return answer