def solution(input_s):
    answer = ''
    num_list = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    
    word = ''
    
    for s in input_s:
        if s.isdigit():     # s가 숫자라면 바로 answer에 추가
            answer += s
            continue
        word += s
        if word in num_list:    # 만든 단어가 숫자 리스트에 있으면 answer에 추가, word 리셋
            answer += str(num_list[word])
            word = ''
            
    answer = int(answer)
    
    return answer