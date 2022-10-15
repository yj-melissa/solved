h_list = [int(input()) for _ in range(9)]

# 부분집합 구하기
for i in range(1<<9):
    lst = []
    for j in range(9):
        if i & (1<<j):
            lst.append(h_list[j])

    h_sum = 0
    if len(lst) == 7 :    # 원소가 7개인 부분집합이라면
        for k in lst:
            h_sum += k
        if h_sum == 100:    # 만일 난쟁이 7명의 키 합이 100인 경우를 찾았다면
            # 집합 오름차순 정렬
            for idx in range(7):
                for jdx in range(7):
                    if lst[idx] < lst[jdx]:
                        lst[idx], lst[jdx] = lst[jdx], lst[idx]
            # 순서대로 정렬
            for idx in lst:
                print(idx)
            break
