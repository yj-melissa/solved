import sys

lst = []
N = int(sys.stdin.readline())
for i in range(N):
    data = list(sys.stdin.readline().split())
    # print(data)

    if data[0] == 'push_back':
        lst.append(int(data[1]))
    elif data[0] == 'push_front':
        lst.insert(0, int(data[1]))
    elif data[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif data[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif data[0] == 'size':
        print(len(lst))
    elif data[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'pop_front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop(0))
    elif data[0] == 'pop_back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop(-1))