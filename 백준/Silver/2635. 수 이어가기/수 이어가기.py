N = int(input())
max_cnt = 0
max_list = []

for i in range(0, N+1):
    n_list = [N, i]    # 두번째 숫자가 i일 때 나오는 숫자 집합
    n = n_list[0] - n_list[1]
    while n >= 0:
        n_list.append(n)
        n = n_list[-2] - n_list[-1]
    if len(n_list) > max_cnt:
        max_cnt = len(n_list)
        max_list = n_list
print(max_cnt)
print(*max_list)