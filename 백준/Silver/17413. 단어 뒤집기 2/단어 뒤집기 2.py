S = input()
stack = [0] * 100001
top = -1
flag = 0    # 괄호 상태 확인
for s in S:
    if flag == 1:    # 괄호가 열린 상태라면 정상 출력
        if s == '>':  # 닫힌 괄호라면 닫힌 괄호 출력후 flag 내림
            print(s, end='')
            flag = 0
        else:
            print(s, end = '')

    else:
        if s == ' ':    # 공백이라면 기존 스택값 전부 pop -> 출력
            while top > -1:
                print(stack[top], end = ''),
                top -= 1
            print(' ', end = '')

        elif s == '<':    # 열린 괄호일 때
            while top > -1:    # 기존 스택 값 전부 출력
                print(stack[top], end = ''),
                top -= 1
            print('<', end = '')
            flag = 1

        else:
            top += 1
            stack[top] = s

while top > -1:     # 스택에 남아있는 문자열 전부 출력
    print(stack[top], end = ''),
    top -= 1

