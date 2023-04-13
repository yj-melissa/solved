N, M = map(int, input().split())    # N : 바구니 갯수, M : 바구니 회전 횟수
buckets = [n for n in range(1, N+1)]        # 바구니 목록

for _ in range(M):
    i, j, k = map(int, input().split())     # i : 회전 시작점, j : 회전 종료점, k : 기준점
    buckets[i-1:j] = buckets[k-1:j] + buckets[i-1:k-1]
print(*buckets)