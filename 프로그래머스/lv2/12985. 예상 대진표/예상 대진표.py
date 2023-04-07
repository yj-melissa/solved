def solution(n,a,b):
    answer = 1

    if a > b:
        a, b = b, a
        
    while True:
        if (a+1) == b and (b%2==0):
            break
        if a % 2:
            a = (a+1)
        if b % 2:
            b = (b+1)
        a //= 2
        b //= 2
        answer += 1
    
    return answer