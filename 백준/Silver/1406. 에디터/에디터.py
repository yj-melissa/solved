import sys

# 1406 에디터

left = list(sys.stdin.readline().rstrip())            # 커서 왼쪽 문자열. readline()은 개행문자가 딸려오는듯?
right = []                      # 커서 오른쪽 문자열
M = int(sys.stdin.readline())
for _ in range(M):
    order = sys.stdin.readline().split()
    if order[0] == 'L' and left:
        right.append(left.pop())
    elif order[0] == 'D' and right:
        left.append(right.pop())
    elif order[0] == 'B' and left:
        left.pop()
    elif order[0] == 'P':
        left.append(order[1])

print(*left, *right[::-1], sep='')