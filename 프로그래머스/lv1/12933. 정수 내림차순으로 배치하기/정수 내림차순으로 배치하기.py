def solution(n):
    answer = 0
    num_list = []
    
    # n을 각 자릿수로 분리 
    for i in str(n):
        num_list += [i]
        
    # 큰 수부터 정렬
    num_list.sort(reverse=True)
    
    # 정렬한 리스트 문자열로 변환
    n = ''
    for i in num_list:
        n += i
    
    # 문자열을 숫자로 변환
    answer = int(n)
    
    return answer