paper = [[0] * 100 for _ in range(100)]     # 100 * 100 도화지
N = int(input())            # 색종이 수

for _ in range(N):
    x, y = map(int, input().split())
    for r in range(10):
        for c in range(10):
            paper[y+r][x+c] = 1

answer = 0
for r in range(100):
    answer += sum(paper[r])
print(answer)