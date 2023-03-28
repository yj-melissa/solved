N = int(input())        # 시험장 개수
A = list(map(int, input().split()))        # 시험장 응시자의 수 Ai
B, C = map(int, input().split())            # 총감독관이 감시하는 응시자의 수, 부감독관이 감시하는 응시자의 수

# 총감독관 1명, 부감독관 여러명(0명 가능)
answer = 0              # 필요한 감독관 수의 최솟값 리턴
for i in range(N):      # 시험장 별 체크
    answer += 1
    if (A[i] - B) > 0:                    # 총감독관이 감시가능한 범위를 넘었을 때
        answer += (A[i] - B) // C         # 총감독관 1명을 제외하고 추가로 필요한 부감독관 수
        if (A[i] - B) % C :                     # 추가로 필요한 부감독관 수 확인
            answer += 1

print(answer)