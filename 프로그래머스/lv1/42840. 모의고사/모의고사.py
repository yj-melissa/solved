def solution(answers):
    answer = []
    point = [0, 0, 0]                 # 답안 
    # 수포자 답안 순서
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    l1, l2, l3 = len(p1), len(p2), len(p3)      # 수포자들의 패턴 길이
    
    for i in range(len(answers)):
        a = answers[i]
        
        # 점수 처리
        if a == p1[i % l1]:
            point[0] += 1
        if a == p2[i % l2]:
            point[1] += 1
        if a == p3[i % l3]:
            point[2] += 1
    
    for i in range(3):
        if point[i] == max(point):
            answer.append(i + 1)
    return answer