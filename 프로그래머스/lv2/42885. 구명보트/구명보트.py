def solution(people, limit):
    answer = 0
    people.sort(reverse=True)             # 몸무게 높은 순 정렬
    e = len(people)-1
    
    for i in range(e+1):
        if people[i] == 250:             # 이미 탄 사람일 때
            continue
        if (i < e) and (people[i] + people[e] <= limit):
            people[e] = 250
            e -= 1
        answer += 1
    
    return answer