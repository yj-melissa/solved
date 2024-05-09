n = int(input())
steps = [0] + [int(input()) for _ in range(n)]
score = [0] * (n + 1)

for i in range(1, n + 1):
    if i < 3:
        score[i] = score[i - 1] + steps[i]
    else:
        score[i] = max(score[i - 3] + steps[i - 1] + steps[i], score[i - 2] + steps[i])

print(score[n])
