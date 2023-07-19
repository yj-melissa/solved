def solution(phone_book):
    answer = True
    
    phone_book.sort()       # 번호순대로 정렬
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
            
        if answer != True:
            return answer
    
    
    
    return answer