def push(x):
    global top
    top += 1
    stack[top] = x

def pop(x):
    global top
    top -= 1
    return stack[top+1]


T = int(input())
for _ in range(T):
    string = list(input())
    stack = [0] * 50    # 문자열의 최대 길이 50
    top = -1
    flag = 0    # YES: 0, NO; 1
    for s in string:
        if s == '(':
            push(s)
        else:
            if top == -1:    # 스택이 비어있는 상태라면 실패
                flag = 1
                break
            elif stack[top] == '(':    # 이미 열린 괄호가 들어 있는 상태라면 ㅇㅋ
                pop(s)
                continue
    else:
        if top > -1:    # 검사를 끝냈는데 남아있는 괄호가 있다면 실패
            flag = 1

    if flag:
        print('NO')
    else:
        print('YES')