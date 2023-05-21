def solution(s):
    answer = 0      # 문자열 개수
    x = ''
    cnt_x = 0       # x가 나온 개수
    cnt_not_x = 0   # x 아닌 문자열이 나온 개수
    
    for i in range(len(s)):
        a = s[i]
        if cnt_x == 0:      # 문자열 처음
            x = a
            cnt_x += 1
            continue
        if a == x:
            cnt_x += 1
        if a != x:
            cnt_not_x += 1
        if cnt_x == cnt_not_x:
            answer += 1
            cnt_x = cnt_not_x = 0
            continue
    return answer if cnt_x == 0 else answer + 1