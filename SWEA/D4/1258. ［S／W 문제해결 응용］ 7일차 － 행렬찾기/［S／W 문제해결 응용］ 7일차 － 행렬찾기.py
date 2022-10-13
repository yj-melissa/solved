T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0    # 찾아낸 행렬 개수
    res = []    # 찾아낸 행렬 정보
    flag = 0
    row = 1
    col = 0

    # 사각형 탐색
    for r in range(N):
        for c in range(N):
            if flag:    # 사각형 탐색 중일 때
                if case[r][c] > 0:    # 사각형이 끝나지 않았다면 col +1
                    col += 1
                    case[r][c] = -1
                if case[r][c] == 0:    # 사각형 종료지점 => 행 크기 확인 필요
                    n_r = r + 1    # row 길이 탐색용
                    c -= 1
                    while 0 <= n_r < N and case[n_r][c] > 0:    # 전체 case 범위 내이고, 사각형이 끝나지 않음
                        for d in range(col):
                            case[n_r][c-d] = -1    # 사각형 범위 내 전부 -1 처리
                        row += 1    # row 길이 1 추가
                        n_r += 1    # 다음 행 탐색
                    res.append([row, col])    # 사각형 범위가 끝나면 사각형 크기 res에 추가.
                    flag = col = 0    # 값 초기화
                    row = 1
            else:    # 사각형 시작점 탐색
                if case[r][c] <= 0:
                    continue
                else:
                    flag = 1
                    cnt += 1
                    col += 1

    # 사각형 크기 비교
    for i in range(cnt-1):
        min_idx = i
        for j in range(i+1, cnt):
            if res[min_idx][0] * res[min_idx][1] > res[j][0] * res[j][1]:
                min_idx = j
        res[i], res[min_idx] = res[min_idx], res[i]


    print(f'#{tc} {cnt}', end = ' ')
    for r in res:
        print(*r, end = ' ')
    print()