def solution(want, number, discount):
    answer = 0
    want_idx = dict()       # want에 포함된 아이템들의 인덱스
    
    for i in range(len(want)):
        want_idx[want[i]] = i
    
    days = [-1] * len(discount)  # days[i] : i번째 날 할인한 아이템의 인덱스
    items = [0] * len(want)     # items[0] : 0번째 아이템이 10일 동안 나온 횟수
    
    for i in range(len(discount)):
        if (i - 10) >= 0 and days[i - 10] > -1:
            items[days[i - 10]] -= 1     # 10일 전 할인한 제품 제외
            
        if discount[i] in want_idx:     # 할인하는 항목이 원하는 제품이었다면 표시
            idx = want_idx[discount[i]]
            items[idx] += 1
            days[i] = idx       
            
        if items == number:     # 사려고 했던 목록과 숫자를 달성했다면 
            answer += 1
        
        
    return answer