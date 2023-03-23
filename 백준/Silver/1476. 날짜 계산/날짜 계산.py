E, S, M = map(int, input().split())
# 1 <= E <= 15, 1 <= S <= 28, 1 <= M <= 19
# 1년 지날 때마다 셋 다 1씩 증가, 범위 넘어가면 1로 돌아감
# 1년 1 1 1 -> 16년 1 16 16

answer = 0                  # 정답
x = y = z = 0               # E, S, M
flag = 1                    # 정답 찾으면 0
while flag:
    answer += 1
    x += 1
    y += 1
    z += 1

    # 범위 벗어났을 때 1로 초기화
    if x > 15:
        x = 1
    if y > 28:
        y = 1
    if z > 19:
        z = 1

    # E, S, M과 동일해졌다면 정답 출력 후 중단
    if (x == E) and (y == S) and (z == M):
        print(answer)
        flag = 0
        break
