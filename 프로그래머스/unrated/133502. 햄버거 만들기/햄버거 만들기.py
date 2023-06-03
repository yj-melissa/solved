def solution(ingredient):
    answer = 0
    stack = []                  # 재료 넣을 스택
    top = -1
    
    for i in ingredient:
        if i == 1 and top > 1:          # 빵이 나오고, stack에 3개 이상 들어있다면
            if (stack[top] == 3) and (stack[top-1] == 2) and (stack[top-2] == 1):   # 햄버거 만들 수 있는지 확인
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
                top -= 3
                continue
                
        stack.append(i)
        top += 1
        
        
    return answer