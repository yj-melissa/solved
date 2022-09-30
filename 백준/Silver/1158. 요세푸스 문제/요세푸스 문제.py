N, K = map(int, input().split())    # N: 사람 수 K: 제거할 간격
circle = [i for i in range(1, N+1)]
res = '<'    # 결과 담을 문자열
i = K-1    # 처음 제거할 사람 인덱스
while circle:    # N명 사람이 다 제거될 때까지 반복되므로
    res += str(circle.pop(i)) + ', '    # 사람 제거 -> 문자열에 추가
    if len(circle) >= 1:
        i = (i + K - 1) % len(circle)    # 원은 처음과 끝이 순회하므로
    else:
        i = 0
res = res[:-2] + '>'    # 출력형식 맞춰주기용
print(res)