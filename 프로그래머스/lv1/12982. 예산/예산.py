import itertools

def solution(d, budget):
    d.sort()                        # 금액 순서대로 정렬
    print(d)
    answer = 0
    total = 0
    for p in d:
        if total + p <= budget:      # 예산 안에서 추가 구매 가능한 경우
            total += p
            answer += 1
    return answer