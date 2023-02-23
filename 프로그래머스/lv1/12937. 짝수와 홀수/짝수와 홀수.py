def solution(num):
    answer = ''
    
    if (num == 0) or (num % 2 == 0):        # num이 0이거나 2로 나눴을 때 나머지가 없다면 짝수
        answer = 'Even'
    else:
        answer = "Odd"
    
    return answer