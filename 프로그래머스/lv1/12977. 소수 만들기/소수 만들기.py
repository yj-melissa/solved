from itertools import combinations
def solution(nums):
    answer = 0
    nums.sort()
    
    # 소수 집합 만들기
    max_sum = sum(nums[-3:])            # 최대 합
    prime = [True] * (max_sum + 1)      # 소수 집합
    for i in range(2, max_sum):
        if prime[i] == False:
            continue
        j = 2
        while (i * j) <= max_sum:
            prime[i * j] = False
            j += 1
    

    # 3개의 수를 더해서 소수인지 판별
    combi = set(map(tuple, combinations(nums, 3)))      # 3개씩 조합한 경우
    
    for c in combi:
        s = sum(c)
        if prime[s] == True:            # 소수라면 answer 집합에 추가
            answer += 1

    return answer