def solution(n):
    answer = -1             # 어떤 수의 제곱이 아니라면 -1 반환
    
    for i in range(1, n+1):
        if i ** 2 == n:
            answer = (i+1) ** 2
            break
    
    return answer