def check_bingo():
    bingo = 0

    # 가로 체크
    for r in range(5):
        if arr[r].count(-1) == 5:
            bingo += 1

    # 세로 체크
    for c in range(5):
        cnt = 0
        for r in range(5):
            if arr[r][c] == -1:
                cnt += 1
        if cnt == 5:
            bingo += 1

    # 정대각선 체크
    cnt = 0
    for i in range(5):
        if arr[i][i] == -1:
            cnt += 1
    if cnt == 5:
        bingo += 1

    # 역대각선 체크
    cnt = 0
    for i in range(5):
        if arr[i][5-i-1] == -1:
            cnt += 1
    if cnt == 5:
        bingo += 1

    if bingo >= 3:
        return 1


def num_check(n):
    for r in range(5):
        for c in range(5):
            if arr[r][c] == n:
                arr[r][c] = -1
                return


arr = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
flag = 0
for i in range(5):
    nums = list(map(int, input().split()))
    if flag:
        continue
    else:
        for j in range(5):
            cnt += 1
            num_check(nums[j])
            bingo = check_bingo()
            if bingo:
                print(cnt)
                flag = 1
                break
