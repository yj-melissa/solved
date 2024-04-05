N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer = M * N

for row in range(N - 8 + 1):        # 인덱스 범위 내에서만 탐색
    for col in range(M - 8 + 1):
        cnt_w = 0       # 시작이 W라고 가정
        cnt_b = 0       # 시작이 B라고 가정
        for dr in range(8):
            for dc in range(8):
                r = row + dr
                c = col + dc
                if (r + c) % 2 == 0:
                    if board[r][c] == 'W':
                        cnt_b += 1
                    else:
                        cnt_w += 1
                else:
                    if board[r][c] == 'B':
                        cnt_b += 1
                    else:
                        cnt_w += 1
        if min(cnt_b, cnt_w) < answer:
            answer = min(cnt_b, cnt_w)

print(answer)