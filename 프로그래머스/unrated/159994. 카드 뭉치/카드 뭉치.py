def solution(cards1, cards2, goal):
    idx_1 = idx_2 = 0
    
    for g in goal:
        if idx_1 < len(cards1) :
            if g == cards1[idx_1]:
                idx_1 += 1
                continue
        if idx_2 < len(cards2) :
            if g == cards2[idx_2]:
                idx_2 += 1
                continue
        return "No"      
    
    return "Yes"