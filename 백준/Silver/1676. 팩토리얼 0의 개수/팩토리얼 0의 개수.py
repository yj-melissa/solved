def factorial(N):
    res = [1] * (N+1)
    n = 2
    while n <= N:
        res[n] = res[n-1] * n
        n += 1
    return str(res[n-1])

N = int(input())
if N < 2:
    print(0)
else:
    num = factorial(N)
    l = len(num)
    cnt = 0
    for i in range(l-1, -1, -1):
        if num[i] == '0':
            cnt += 1
        else:
            print(cnt)
            break
    else:
        print(cnt)
