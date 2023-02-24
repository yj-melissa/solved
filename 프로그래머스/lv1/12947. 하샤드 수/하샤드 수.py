def solution(x):
    answer = False
    
    str_x = str(x)
    sum_num = 0                 # 자릿수 합
    for n in str_x:            # 각 자리수 합 더함
        sum_num += int(n)
    
    if x % sum_num == 0:        # 하샤드 수 판별
        answer = True
    
    return answer