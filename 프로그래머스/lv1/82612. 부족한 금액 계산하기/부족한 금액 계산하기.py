def solution(price, money, count): 
    
    for c in range(1, count+1):
        money -= price * c
        print(money)
        
    if money > 0:
        answer = 0
        
    else:
        answer = -money

    return answer