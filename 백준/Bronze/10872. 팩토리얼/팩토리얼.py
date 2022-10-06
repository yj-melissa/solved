N = int(input())

res = [0]*(N+1)
def factorial(N):
    if N == 0 or N == 1:
        res[N] = 1
    else:
        factorial(N-1)
        res[N] = res[N-1] * N
    return res[N]

print(factorial(N))