def solution(k, score):
    ranking = []
    answer = []
    
    for s in score:
        ranking.append(s)
        ranking.sort(reverse = True)
        ranking = ranking[:k]
        answer.append(ranking[-1])
    
    return answer