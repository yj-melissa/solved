def solution(s):    
    answer = 0
    stack = []
    top = -1
    
    
    for _ in range(len(s)):
        s = s[1:] + s[:1]
    
        for bracket in s:
            if bracket in ["[", "(", "{"]:      # 여는 괄호라면 스택에 추가
                stack.append(bracket)
                top += 1
                continue

            if top < 0:                         # 닫는 괄호인데 스택이 비어있으면 문자열 만들 수 없음
                break

            if bracket == "]" and stack[top] == "[":
                stack.pop()
                top -= 1
                continue

            if bracket == ")" and stack[top] == "(":
                stack.pop()
                top -= 1
                continue

            if bracket == "}" and stack[top] == "{":
                stack.pop()
                top -= 1
                continue

            break
            
        else:
            if top == -1:
                answer += 1
            
    
    return answer