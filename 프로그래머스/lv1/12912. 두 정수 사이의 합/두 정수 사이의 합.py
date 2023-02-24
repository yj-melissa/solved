def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    else:
        if a > b:         # a가 b보다 크다면 둘 순서 바꿈
            a, b = b, a
        for i in range(a, b+1):
            answer += i
    
    return answer