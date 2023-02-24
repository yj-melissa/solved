def solution(n):
    for x in range(1, n):       # 작은 수부터 나누기 시작
        if n % x == 1:          # 나머지가 1인 수가 나오면 answer로 반환
            return x