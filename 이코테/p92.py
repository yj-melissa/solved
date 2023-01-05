# 이코테 p.92 큰 수의 법칙

import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())     # 배열크기 N, 숫자 더해지는 횟수 M, 연속 더할 수 있는 횟수 K
arr = list(map(int, input().split()))   # 주어진 배열
arr.sort()  # 배열 오름차순 정렬

max_sum = 0       # 최대로 더한 값
cnt = 0           # 연속으로 더한 값

for i in range(M):  # M번 동안 더함
    if cnt < K:     # 연속으로 더한 횟수
        max_sum += arr[-1]
        cnt += 1
    else:
        max_sum += arr[-2]
        cnt = 0

print(max_sum)

