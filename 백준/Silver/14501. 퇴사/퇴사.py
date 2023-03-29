N = int(input())            # 주어진 날짜
tp_list = [list(map(int, input().split())) for _ in range(N)]       # tp_list[0] = [1일차의 상담 기간, 금액]

dp = [0] * (N+1)                      # 이익 기록 리스트. index 문제로 1칸 더 만듦.
for d in range(N-1, -1, -1):            # 역순으로 진행
    t, p = tp_list[d][0], tp_list[d][1]
    if (d + t) > N:             # 퇴사일을 초과하면 상담 불가
        dp[d] = dp[d+1]         # 중간에 너무 긴 길이가 나왔을 때 대비
        continue
        
    if dp[d+1] > dp[d+t] + p:            # d 일에 일을 하는 것 보다 다른 날에 버는 수익이 더 많다면 일 x. dp[d] = dp[d+1]
        dp[d] = dp[d+1]

    else:
        dp[d] = dp[d+t] + p

print(dp[0])
