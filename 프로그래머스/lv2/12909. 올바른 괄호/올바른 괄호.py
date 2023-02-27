def solution(string):
    top = -1        # 열린 괄호 갯수 확인
    
    for s in string:
        if s == '(':
            top += 1
        
        else:       # 닫힌 괄호일 때
            if top > -1:        # 열린 괄호가 있으면
                top -= 1        # 열린 괄호 갯수 -1
            else:
                return False  # 열린 괄호가 없으면 False
                
    if top > -1:        # 남은 괄호가 있으면 false
        return False
    else:
        return True