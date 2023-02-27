def solution(s):
    answer = ""
    flag = 0        # 공백이 나오면 플래그 0
    
    for w in s:
        if flag:
            if w == " ":    # 단어 후 공백 등장: flag down
                flag = 0
                answer += w
            else:
                answer += w.lower()
            continue
            
        if flag == 0:
            if w == " ":
                answer += w
            else:
                flag = 1    # 공백 다음 첫 문자: 플래그 on, 대문자 처리
                answer += w.upper()
            continue
    
    return answer