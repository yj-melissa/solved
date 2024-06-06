N = int(input())
buildings = [int(input()) for _ in range(N)]
answer = 0
stack = []

for i in range(N):
    while stack:
        if buildings[stack[-1]] <= buildings[i]:
            stack.pop()
        else:
            break
    answer += len(stack)
    stack.append(i)

print(answer)