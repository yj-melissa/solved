def solution(s):
    answer = ''
    s_length = len(s)
    
    if s_length % 2 :       # s 길이가 홀수라면
        answer = s[s_length//2]
    else:
        answer = s[s_length//2-1:s_length//2+1]
    return answer