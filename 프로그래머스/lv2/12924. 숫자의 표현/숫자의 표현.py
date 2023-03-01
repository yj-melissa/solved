def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        total = 0          # 연속된 수를 더한 숫자
        for j in range(i, n+1):
            total += j
            if total == n:      # total이 n과 일치하면 answer +1
                answer += 1
                break
            elif total > n:     # total이 n을 초과하면 중단
                break
    return answer