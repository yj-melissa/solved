N = int(input())
formula = list(input())
N_list = [int(input()) for _ in range(N)]
stack = [0] * 100
top = -1


for f in formula:
    if f.isalpha():    # 피연산자라면 push
        top += 1
        stack[top] = N_list[ord(f) - 65]    # 피연산자를 숫자로 바꿔줘야함 / ord('A') == 65

    else:              # 연산자라면 피연산자 pop
        B = stack[top]
        top -= 1
        A = stack[top]
        top -= 1
        # 연산 후 다시 push
        top += 1
        if f == '+':
            stack[top] = A + B
        elif f == '-':
            stack[top] = A - B
        elif f == '*':
            stack[top] = A * B
        elif f == '/':
            stack[top] = A / B

res = stack[top]
print(f'{res:.2f}')