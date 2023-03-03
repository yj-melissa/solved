def solution(n):
    f_list = [0, 1]
    for f in range(2, n+1):
        f_list.append(f_list[f-1]+f_list[f-2])
    answer = f_list[f] % 1234567
    return answer