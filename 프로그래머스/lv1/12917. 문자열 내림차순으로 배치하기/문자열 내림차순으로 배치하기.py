def solution(s):
    answer = ''
    s_length = len(s)
    s_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    b_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for ba in b_alphabets:          # 대문자: 늦게 추가될 수록 앞에 추가됨
        if s.count(ba):
            answer = ba*s.count(ba) + answer
    
    for sa in s_alphabets:          # 소문자: 늦게 추가될 수록 앞에 추가됨
        if s.count(sa):
            answer = sa*s.count(sa) + answer
    
    
    return answer