def solution(s):
    answer = [-1] * len(s)
    
    for i in range(1, len(s)):
        for j in range(1, i+1):       # 앞에 나온 글자들만 가까운 순부터 조사
            if s[i] == s[i-j]:      # 같은 글자가 있다면 거리 반영
                answer[i] = j
                break        
        
    return answer