def solution(s):
    
    answer = ''
    cnt = 0         # 단어 자리 수 확인
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            cnt = 0
            continue
            
        if cnt == 0 or cnt % 2 == 0:
            answer += s[i].upper()
        
        else:
            answer += s[i].lower()
        cnt += 1
            
                
    return answer