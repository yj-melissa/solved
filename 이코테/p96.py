# 이코테 p.96 숫자 카드 게임

import sys

sys.stdin = open('../../input.txt')

T = int(input())        # 테스트케이스 개수

for tc in range(T):
    N, M = map(int, input().split())        # 행 N, 열 M
    arr = [list(map(int, input().split())) for _ in range(N)]       # 카드 배열

    # 각 행에서 가장 작은 숫자 확인
    min_num = []        # 각 행에서 가장 작은 숫자 담을 리스트
    for i in range(N):
        min_num.append(min(arr[i]))

    # 그 중 가장 큰 숫자 선택
    print(max(min_num))


# 습관적으로 입력 배열을 저장하고 봤는데, 각 행을 받자마자 가장 작은 수를 찾아내 그 중 큰 수를 발견하는 방법도 있었다.