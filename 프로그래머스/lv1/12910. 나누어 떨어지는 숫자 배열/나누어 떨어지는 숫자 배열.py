def solution(arr, divisor):
    answer = []
    
    if divisor == 1:
        answer = arr
    else:
        for num in arr:
            if num % divisor == 0:
                answer.append(num)
    if answer:
        answer.sort()
    else:
        answer = [-1]
    
    return answer