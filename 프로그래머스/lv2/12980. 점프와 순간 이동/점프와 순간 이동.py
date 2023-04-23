def solution(N):
    battery = 0
    while N > 0:
        battery += N % 2
        N //= 2
        
    return battery