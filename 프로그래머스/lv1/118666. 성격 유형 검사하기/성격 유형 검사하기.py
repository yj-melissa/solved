def solution(survey, choices):
    answer = ''
    indicators = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}       # 유형별 점수
    
    
    # 유형 별 점수 확인
    for i in range(len(survey)):
        c = choices[i]
        if c < 4:       # 비동의일 때
            indicators[survey[i][0]] += (4 - c) 
            continue
        
        if c == 4:    # 모르겠다일 때
            continue
        
        if c > 4:       # 동의일 때
            indicators[survey[i][1]] += (c - 4)
            
    # 성격 유형 확인 : 한 지표에서 성격 유형 점수 같으면 사전순으로 빠른 성격 유형 선택
    answer += 'R' if indicators['R'] >= indicators['T'] else 'T'
    answer += 'C' if indicators['C'] >= indicators['F'] else 'F'
    answer += 'J' if indicators['J'] >= indicators['M'] else 'M'
    answer += 'A' if indicators['A'] >= indicators['N'] else 'N'
    
        
    return answer