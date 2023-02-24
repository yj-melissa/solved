def solution(num):
    answer = 0
    
    while (num != 1) & (answer < 500):
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        answer += 1
    
    if (answer == 500) and (answer != 1):
        answer = -1
        
    return answer