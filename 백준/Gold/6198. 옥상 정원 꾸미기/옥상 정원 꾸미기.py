N = int(input())
buildings = [int(input()) for _ in range(N)]
answer = 0
stack = []

for i in range(N):
    while stack:
        j = stack.pop()
        if buildings[j] <= buildings[i]:        # 지금 건물이 더 높거나 같음
            answer += (i - j - 1)
        else:
            stack.append(j)
            break
    stack.append(i)

while stack:
    i = stack.pop()
    answer += (N - 1 - i)

print(answer)