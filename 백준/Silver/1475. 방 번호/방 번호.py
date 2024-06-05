import math

N = input()

cnt = [0] * 9

for n in N:
    num = int(n)
    if num == 9:
        num = 6
    cnt[num] += 1

cnt[6] = math.ceil(cnt[6] / 2)

print(max(cnt))

