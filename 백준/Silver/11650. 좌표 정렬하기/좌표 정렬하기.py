N = int(input())
codes = [list(map(int, input().split())) for _ in range(N)]
codes = sorted(codes, key=lambda code:(code[0], code[1]))
for i in range(N):
    print(*codes[i])