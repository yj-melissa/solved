def solution(strings, n):
    answer = []
    n_alpha = dict()
    
    # n번째 글자만 모은 리스트 생성 -> 정렬    
    for s in strings:
        if s[n] in n_alpha:
            n_alpha[s[n]].append(s)
        else:
            n_alpha[s[n]] = [s]
    
    
    # 순서대로 answer에 추가
    for i in range(ord('a'), ord('z')+1):
        if chr(i) in n_alpha:
            n_alpha[chr(i)].sort()
            answer += n_alpha[chr(i)]
    
    return answer