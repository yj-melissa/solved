def solution(s):   
    answer = True
    num_p = num_y = 0       # s에 포함된 p와 y의 개수

    for a in s:
        if a == 'p' or a == 'P':
            num_p += 1
        elif a == 'y' or a == 'Y':
            num_y += 1
    
    if num_p != num_y:      # p와 y 개수가 다를 때만 False
        answer = False

    return answer