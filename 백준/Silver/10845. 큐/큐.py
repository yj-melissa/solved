import sys

N = int(sys.stdin.readline())
Q = [0] * 10001
frnt = -1
rear = -1
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        rear += 1
        Q[rear] = order[1]

    elif order[0] == 'pop':
        if -1 <= frnt < rear:
            frnt += 1
            print(Q[frnt])
        else:
            print(-1)

    elif order[0] == 'size':
        print(rear - frnt)

    elif order[0] == 'empty':
        if frnt == rear:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if frnt >= rear:
            print(-1)
        else:
            print(Q[frnt+1])

    elif order[0] == 'back':
        if frnt == rear:
            print(-1)
        else:
            print(Q[rear])