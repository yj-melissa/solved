def cnt_binary(n):
    cnt = 0          # 2진법으로 변환한 n의 1의 갯수
    while n >= 1:
        if n%2:      # 1이라면 cnt +1
            cnt += 1
        n //= 2
    return cnt    


def solution(n):
    answer = n + 1
    n_cnt = cnt_binary(n)
    
    while True:
        if cnt_binary(answer) == n_cnt:
            break
        answer += 1
        
    
    return answer