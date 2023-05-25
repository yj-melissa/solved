def solution(numbers, hand):
    answer = ''
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    loc = dict()        # 키패드 위치
    
    for i in range(4):
        for j in range(3):
            loc[pad[i][j]] = (i, j)
    
    L, R = '*', '#'     # 왼손, 오른손 위치
    
    for n in numbers:
        if (n == 1) or (n == 4) or (n == 7):
            answer += 'L'
            L = n
            continue    
            
        if (n == 3) or (n == 6) or (n == 9):
            answer += 'R'
            R = n
            continue
            
        # 가까운 엄지 확인
        nr, nc = loc[n]
        l_cnt = abs(loc[L][0] - nr) + abs(loc[L][1] - nc)       # 왼손 움직이는 횟수
        r_cnt = abs(loc[R][0] - nr) + abs(loc[R][1] - nc)       # 오른손 움직이는 횟수

        if l_cnt < r_cnt:
            answer += 'L'
            L = n
            continue
            
        if r_cnt < l_cnt:
            answer += 'R'
            R = n
            continue
            
        if hand == "left":
            answer += 'L'
            L = n
            
        else:
            answer += 'R'
            R = n
        
            
    return answer