stick = input()         # 쇠막대기
stack = []
cnt = 0
flag = 0            # 레이저 판별 여부
for s in stick:
    if s == '(':
        stack.append('(')
        flag = 1
    elif s == ')':
        if flag == 1:       # 여는 괄호와 인접한 닫는 괄호
            flag = 0
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)