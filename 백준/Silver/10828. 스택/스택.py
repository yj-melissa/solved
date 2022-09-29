import sys
N = int(sys.stdin.readline())
stack = []
top = -1
for _ in range(N):
    order = list(sys.stdin.readline().split())        # push는 입력으로 숫자 같이 들어오므로

    if order[0] == 'push':
        stack.append(order[1])
        top += 1
        continue

    elif order[0] == 'pop':
        if top == -1 :
            print(-1)
        else:
            print(stack.pop())
            top -= 1
        continue

    if order[0] == 'size':
        if top <= -1:
            print(0)
        else:
            print(top+1)
        continue

    if order[0] == 'empty':
        if top <= -1:
            print(1)
        else:
            print(0)
        continue

    if order[0] == 'top':
        if top <= -1:
            print(-1)
        else:
            print(stack[top])
        continue