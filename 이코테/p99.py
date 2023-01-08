# p.99 1이 될 때까지

import sys

sys.stdin = open('../../input.txt')

N, K = map(int, input().split())

cnt = 0     # 연산 횟수

while N != 1:        # N이 1이 될 때까지 반복
    # N이 K의 배수가 아니라면 -1 연산
    if N % K != 0:
        N -= 1
        cnt += 1

    # N이 K의 배수라면 N // K
    else:
        N /= K
        cnt += 1

print(cnt)


# 알고리즘 오래 쉬었더니 쉬운 방법으로만 풀게 되는듯..
# 문제에 주어진 대로만 푸는 게 아니라 책처럼 더 빠른 방법을 생각하려고 고민해봐야겠음