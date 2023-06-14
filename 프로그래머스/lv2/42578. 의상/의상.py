def solution(clothes):
    categories = dict()
    answer = 1
    
    for i in range(len(clothes)):
        cloth, category = clothes[i]
        if category in categories:      # 종류별로 옷 추가
            categories[category].append(cloth)
        else:
            categories[category] = [cloth]
    
    for c in categories:
        answer *= (len(categories[c]) + 1)
        
    
    return answer - 1               # 아무것도 안 입는 경우 제외