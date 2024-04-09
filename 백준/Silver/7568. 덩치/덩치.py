import sys

N = int(input())
data = [0] * N
for i in range(N):          # 몸무게, 키 데이터 입력
    x, y = map(int, input().split())
    data[i] = (x, y)

compare_result = [0] * N
for i in range(N):          # 덩치 비교
    x1, y1 = data[i]
    for j in range(i + 1, N):
        x2, y2 = data[j]
        if (x1 > x2) and (y1 > y2):     # 첫번째 덩치가 더 큰 경우
            compare_result[j] += 1
        elif (x1 < x2) and (y1 < y2):   # 두 번째 경치가 더 큰 경우
            compare_result[i] += 1
            
for i in range(N):
    print(compare_result[i] + 1, end = ' ')