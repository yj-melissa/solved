def solution(a, b, n):      # a: 마트에 줘야하는 콜라 수, b: 마트가 주는 콜라 수, n: 가진 콜라 수
    answer = 0
    while n >= a:       
        c = b * (n // a)        # 마트로부터 받을 병 수
        n %= a                  # 병 교환
        n += c
        answer += c
        
        
    return answer