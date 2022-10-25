N = 5
scores = [list(map(int, input().split())) for _ in range(N)]
max_idx = max_score = 0

for i in range(N):
    total = 0
    for j in range(4):
        total += scores[i][j]
    if total > max_score :
        max_score = total
        max_idx = i + 1
print(max_idx, max_score)