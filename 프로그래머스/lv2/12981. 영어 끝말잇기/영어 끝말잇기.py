def solution(n, words):
    answer = [0, 0]                 # 탈락자 생기지 않으면 [0, 0] 리턴
    
    # 1~n번이 돌아가면서 words 순서대로 말함
    for i in range(len(words)):
        flag = 0                    # 탈락시 flag on
        
        if i > 0:
            # 앞의 단어 마지막 문자와 이번 단어 첫 글자가 다르면 실패
            if words[i-1][-1] != words[i][0]:
                flag = 1
            
            # 이전의 단어와 동일하면 실패
            if words[:i].count(words[i]) > 0:
                flag = 1     
            
        # 한 글자는 인정x
        if len(words[i]) == 1:
            flag = 1
        
        # 가장 먼저 탈락하는 사람의 번호와 그 사람이 '자신의' 몇 번째 차례에 탈락하는지 구해서 리턴
        if flag:                    # 탈락하면 answer값 수정
            answer = [i%n+1, i//n+1]
            break

    return answer