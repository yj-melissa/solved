import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    password = input().strip()
    left = []
    right = []

    for p in password:
        if p == '-':        # 백스페이스
            if left:
                left.pop()
        elif p == '<':     # 커서이동
            if left:
                right.append(left.pop())
        elif p == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(p)

    left.extend(reversed(right))

    print(''.join(left).strip())