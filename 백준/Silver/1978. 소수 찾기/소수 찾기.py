N = int(input())
num_list = list(map(int, input().split()))
cnt = 0
for i in range(N):
    n = num_list[i]
    if n == 1:
        continue
    elif n <= 3:
        cnt += 1
    elif n % 2:    # 2이상 짝수는 소수가 아님
        for j in range(3, n):
            if n % j == 0:
                break
        else:
            cnt += 1
print(cnt)