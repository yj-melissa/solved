def solution(t, p):
    answer = 0
    lp = len(p)
    num = int(p)
    # t의 부분 문자열 중 p와 길이가 같은 문자열 확인
    for i in range(len(t)-lp+1):
        # t의 부분 문자열이 p보다 작거나 같으면 answer += 1
        if int(t[i:i+lp]) <= num:
            answer += 1
            
    return answer