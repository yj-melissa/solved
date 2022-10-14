def range_check(r, c):
    if 0 <= r < R and 0 <= c < C and arr[r][c] == 0:
        return True

C, R = map(int, input().split())    # 좌석 가로, 세로
K = int(input())    # 고객 수

if K > C*R :    # 고객 번호가 좌석 수보다 크면 좌석 배정 불가.
    print(0)
else:
    arr = [[0] * C for _ in range(R)]
    dr = [-1, 0, 1, 0]    # 상우하좌
    dc = [0, 1, 0, -1]
    di = 0
    r, c = R-1, 0    # 시작점
    k = 1    # 배정한 좌석 수
    while k <= K:
        if range_check(r, c):
            arr[r][c] = k
            if k == K:
                print(c + 1, R - r)
                break
            k += 1
            r = r + dr[di % 4]
            c = c + dc[di % 4]
        else:
            r, c = r - dr[di % 4], c - dc[di % 4]
            di += 1
            r, c = r + dr[di % 4], c + dc[di % 4]