def solution(s):
    answer = ""
    
    for a in s:
        if len(answer) == 0 or answer[-1] == " ":
            answer += a.upper()
        else:
            answer += a.lower()
    
    return answer