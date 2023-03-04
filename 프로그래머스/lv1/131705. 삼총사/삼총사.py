import itertools

def solution(number):
    answer = 0
    combi = itertools.combinations(number, 3)       # 원소 3개를 이용한 부분집합
    for c in combi:
        if sum(c) == 0:     # 3명 합이 0이라면 answer +1
            answer += 1
    return answer