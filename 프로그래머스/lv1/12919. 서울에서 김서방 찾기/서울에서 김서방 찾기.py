def solution(seoul):
    answer = ''
    for i in range(1000):
        if seoul[i] == "Kim":
            answer = f'김서방은 {i}에 있다'
            break
    return answer