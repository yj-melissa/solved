def solution(arr):
    answer = 0              # 답안
    length = len(arr)    # arr의 길이
    total = 0               # arr에 들어있는 수의 합
    
    for i in range(length):     # total 을 구함
        total += arr[i]
    answer = total / length     # arr에 들어있는 수의 합 / arr의 길이
    
    return answer