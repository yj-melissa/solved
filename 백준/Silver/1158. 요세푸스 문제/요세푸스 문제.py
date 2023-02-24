N, K = map(int, input().split())     # N : 사람 수, K(<=N) : K번째 사람 제거

people = [i for i in range(1, N+1)]         # 원을 이룬 사람 수
answer = "<"                       # 요세푸스 순열
killed = 0                        # 사람 제거한 횟수
now = K-1                        # 제거할 사람 위치

while killed < N:
    answer += str(people[now])
    people.pop(now)                 # 제거한 사람은 리스트에서도 제거
    killed += 1
    if killed == N:
        answer += ">"
        break
    now += K-1
    while now >= (N-killed):
        now -= (N-killed)

    answer += ", "

print(answer)