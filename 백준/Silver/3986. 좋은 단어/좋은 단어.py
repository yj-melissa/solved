N = int(input())
words = list(input() for _ in range(N))

answer = 0

stack = [0] * 100000        # 단어의 최대 길이
top = -1

for i in range(N):

    word = words[i]

    for w in word:      # 좋은 단어 검사
        if top == -1 or stack[top] != w:       # 스택이 비어 있거나 직전 단어와 다름
            top += 1
            stack[top] = w
        else:
            top -= 1

    if top == -1:       # 검사 끝난 후 스택이 비어있으면 좋은 단어 +1
        answer += 1

    top = -1        # 스택 초기화

print(answer)
