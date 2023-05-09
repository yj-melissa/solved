def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)      # 가격 높은 순대로 정렬
    e = m - 1                       # 각 상자별 최저 사과 인덱스
    while e < len(score):
        answer += score[e] * m
        e += m
    return answer