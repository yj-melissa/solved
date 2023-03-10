def solution(s):
    stack = []
    
    for a in s:
        if stack and stack[-1] == a:        # 스택 맨 위에 있는 알파벳과 같으면 pop
                stack.pop()
        else:
            stack.append(a)
    if stack:
        return 0
    return 1