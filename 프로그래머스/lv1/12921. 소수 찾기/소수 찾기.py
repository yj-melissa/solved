def solution(n):
    answer = [True] * (n+1)         # 인덱스, 실제 수 맞춰주기 위함
    
    for i in range(2, n):                # 짝수 제외
        if answer[i] == False:
            continue
        j = 2
        while (i * j) <= n:
            answer[i * j] = False
            j += 1
    return answer.count(True) - 2           # 0, 1 제외