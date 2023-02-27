# 9012_괄호

T = int(input())
for _ in range(T):
    stack = [0] * 50        # 문자열 길이(2 <= x <= 50)
    top = -1
    string = input()
    answer = "YES"

    for s in string:
        if s == '(':
            top += 1
            stack[top] = '('

        elif s == ')':
            if top >= 0:
                top -= 1
            else:               # 닫는 괄호가 여는 괄호보다 많으면 문자열 x
                answer = "NO"
                break

    if top != -1 :        # 문자열이 끝났을 때 스택이 남아있으면 문자열x
        answer = "NO"

    print(answer)