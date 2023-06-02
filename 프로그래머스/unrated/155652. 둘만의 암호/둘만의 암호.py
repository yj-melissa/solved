def check_range(a):             # a 범위 확인
    if a > 122:
        a -= 26
    return a

def solution(s, skip, index):
    answer = ''
    
    skip_list = []              # 건너뛸 알파벳 번호
    for sk in skip:
        skip_list.append(ord(sk)) 
    
    for alphabet in s:
        # 문자열 숫자로 바꿈
        a = ord(alphabet)

        # index만큼 더함
        for i in range(index):
            a += 1
            a = check_range(a)
            
            while a in skip_list:
                a += 1
                a = check_range(a)
        
        answer += chr(a)
        
    
    return answer