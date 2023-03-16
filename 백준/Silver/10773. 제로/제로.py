K = int(input())

num_list = [0] * K
top = -1

for _ in range(K):
    num = int(input())
    if num == 0:        # 최근 숫자를 지움
        num_list[top] = 0
        top -= 1

    else:
        top += 1
        num_list[top] = num

print(sum(num_list))