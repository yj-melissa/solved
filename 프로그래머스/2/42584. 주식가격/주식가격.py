def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            before = stack.pop()
            answer[before] = i - before
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - 1 - idx
        
        
    
    return answer