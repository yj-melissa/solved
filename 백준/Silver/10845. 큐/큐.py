import sys

N = int(input())        # 주어지는 명령의 수

queue = []

for _ in range(N):      # 명령의 수 N번만큼 반복
    order = sys.stdin.readline().split()     # 주어진 명령 : 공백 기준으로 슬라이스, 리스트에 저장.
                                            # input()쓰면 시간 초과남
    word = order[0]         # 수행할 명령

    if word == 'push':      # 정수 X(order[1])를 큐에 추가
        queue += [int(order[1])]

    elif word == 'pop':     # 큐에서 가장 앞에 있는 정수 빼서 출력. 큐가 빈 경우에는 -1 출력
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

    elif word == 'size':    # 큐에 들어있는 정수의 개수 출력
        print(len(queue))

    elif word == 'empty':   # 큐가 비어있으면 1, 아니면 0 출력
        if queue:
            print(0)
        else:
            print(1)

    elif word == 'front':   # 큐 가장 앞에 있는 정수 출력. 큐가 비어있으면 -1 출력
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif word == 'back':    # 큐 가장 뒤에 있는 정수 출력. 큐가 비어있으면 -1 출력
        if queue:
            print(queue[-1])
        else:
            print(-1)
