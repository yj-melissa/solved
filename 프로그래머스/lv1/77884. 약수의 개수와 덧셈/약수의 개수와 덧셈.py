def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        cnt = 0                     # 약수의 갯수
        for i in range(1, num+1):
            if num % i == 0:        # 약수에 해당하면 카운트
                cnt += 1
        if cnt % 2:                 # 약수가 홀수개라면 빼고 
            answer -= num
        else:                       # 약수가 짝수개라면 더함
            answer += num
            
    return answer