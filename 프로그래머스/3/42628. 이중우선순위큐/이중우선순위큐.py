import heapq

def solution(operations):
    answer = [0] * 2
    h = []
    
    for operation in operations:
        order, num = operation.split()
        num = int(num)
        
        if order == "I":
            heapq.heappush(h, num)
            continue
        if h:
            if num == 1:
                h.pop()
            else:
                heapq.heappop(h)
        
    if h:
        answer[0] = max(h)
        answer[1] = min(h)
    
    return answer