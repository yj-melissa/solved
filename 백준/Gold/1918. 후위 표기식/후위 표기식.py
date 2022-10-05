formula = list(input())
stack = [0] * 100    # 식의 길이가 100을 넘지 않음
top = -1
res = ''

# 스택에 넣을 때 우선 순위
icp = {
    ')' : 0,
    '*' : 2,
    '/' : 2,
    '+' : 1,
    '-' : 1,
    '(' : 3
}
# 스택에 있을 때 우선 순위
isp = {
    ')' : 0,
    '*' : 2,
    '/' : 2,
    '+' : 1,
    '-' : 1,
    '(' : 0
}

# 후위표기로 변환
for f in formula:
    if f.isalpha():
        res += f
    else:
        if top < 0 or isp[stack[top]] < icp[f]:    # 스택이 비어있거나 들어갈 연산자 순위가 높으면 push
            top += 1
            stack[top] = f
        else:
            if f == ')':    # 닫는 괄호를 만나면 여는 괄호를 만날 때까지 pop해서 출력
                while stack[top] != '(':
                    res += stack[top]
                    top -= 1
                top -= 1    # 여는 괄호는 출력하지 않고 pop
            else:           # 그 외 연산자라면
                while top > -1 and isp[stack[top]] >= icp[f]:    # 들어갈 연산자 순위가 낮으면 우선 순위 높아질 때까지 기존 연산자 pop
                    res += stack[top]
                    top -= 1
                top += 1
                stack[top] = f

# 스택에 남은 연산자 전부 출력
while top > -1:
    res += stack[top]
    top -= 1

print(res)