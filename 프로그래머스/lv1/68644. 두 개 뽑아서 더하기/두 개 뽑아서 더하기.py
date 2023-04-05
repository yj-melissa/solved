def solution(numbers):
    answer = []
    numbers.sort()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    answer = list(set(answer))          # 중복 제거
    answer.sort()
    return answer