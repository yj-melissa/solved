import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]
stack = []
answer = 0

for i in range(N):
    cnt = 1

    while stack and stack[-1][0] <= heights[i]:
        h, c = stack.pop()
        answer += c

        if h == heights[i]:     # 키가 같은 경우
            cnt += c

    if stack:
        answer += 1

    stack.append((heights[i], cnt))

print(answer)
