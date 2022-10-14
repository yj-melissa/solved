N = int(input())
lst = list(map(int, input().split()))
max_l = 0
l = 1

# 수열 안에서 연속해서 커지는 경우
for i in range(1, N):
    if lst[i-1] <= lst[i]:
        l += 1
    else:
        if l > max_l:
            max_l = l
        l = 1
if l > max_l:
    max_l = l

# 연속해서 작아지는 경우
l = 1
for i in range(1, N):
    if lst[i-1] >= lst[i]:
        l += 1
    else:
        if l > max_l:
            max_l = l
        l = 1
if l > max_l:
    max_l = l

print(max_l)