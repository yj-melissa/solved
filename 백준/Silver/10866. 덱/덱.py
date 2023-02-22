import sys

N = int(input())        # 주어지는 명령의 수
deque = [0] * N
front = end = 0

for i in range(N):      # 명령 수만큼 반복
    order = list(sys.stdin.readline().split())        # input() 쓰면 시간초과. readline() 쓰면 통과함.
    order_word = order[0]

    if order_word == 'push_front':
        num = int(order[1])
        if front == end:
            deque[front] = num
            end += 1
        elif 0 < front < end:
            deque[front - 1] = num
            front -= 1
        else:
            deque.insert(front, num)
            end += 1

    elif order_word == 'push_back':
        num = int(order[1])
        deque[end] = num
        end += 1

    elif order_word == 'pop_front':
        if front == end:
            print(-1)
        else:
            print(deque[front])
            front += 1

    elif order_word == 'pop_back':
        if front == end:
            print(-1)
        else:
            end -= 1
            print(deque[end])

    elif order_word == 'size':
        print(end - front)

    elif order_word == 'empty':
        if front == end:
            print(1)
        else:
            print(0)

    elif order_word == 'front':
        if (front == end) or (front == -1):
            print(-1)
        else:
            print(deque[front])

    elif order_word == 'back':
            if front == end:
                print(-1)
            else:
                print(deque[end - 1])


