def solution(n):
    fib = [0] * n
    
    for i in range(n):
        if i == 0:
            fib[i] = 1
        elif i == 1:
            fib[i] = 2
        else:
            fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n-1] % 1234567