def solution(n):
    if n == 0:              # n == 0이라면 바로 리턴
        return 0
    
    else:
        answer = 0          # n의 약수를 모두 더한 값

        for i in range(1, n+1):      # 1부터 n까지 검사
            if n % i == 0:         # n을 i로 나눴을 때 나머지가 0이면 i는 n의 약수
                answer += i

        return answer