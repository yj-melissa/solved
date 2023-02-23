def solution(x, n):
    answer = []
    
    for i in range(1, n+1):         # i -> 1부터 n까지 반복
        answer += [x * i]           # x * i한 값을 answer 리스트에 추가 
        
    return answer