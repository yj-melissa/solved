sticks = input()        # 쇠막대기

top = -1
flag = 1       # 1 : 직전까지 여는 괄호, -1 : 닫는 괄호
answer = 0

for s in sticks:
    if s == '(':
        top += 1
        flag = 1

    else:
        top -= 1
        if flag == 1:    # 레이저
            answer += top + 1
        else:
            answer += 1
        flag = -1

print(answer)
