def solution(dartResult):
    answer = 0
    
    dartResult = dartResult.replace('10', 'x')      # 10이 있다면 x로 교체
    stack = list(dartResult)
    option = 0                  # 스타상: 2, 아차상 -1
    
    # S : **1, D : **2, T : **3
    
    while stack:
        s = stack.pop()
        
        # 옵션 확인
        if s == '*':
            option = 2 if option == 0 else 3        # 스타상 중첩되는 상황이라면 3
            continue
        if s == '#':
            option = -1 if option == 0 else -2      # 스타상과 중첩되는 경우 -2
            continue
        
        score = stack.pop()
        score = 10 if score == 'x' else int(score)
        
        if s == 'D':
            score **= 2
        elif s == 'T':
            score **= 3
        
        if option > 0:            # 스타상
            if option > 2:       # 스타상 중첩된 경우
                score *= 4
                option = 1
            else:
                score *= 2
                option -= 1
        elif option < 0:        # 아차상
            if option == -1:
                score = -score
            elif option == -2:      # 아차상 + 스타상
                score = -score * 2
            option = 0
        answer += score
        
            
    return answer