def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    ranking = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}        # 순위
    
    cnt_zero = 0        # 알아볼 수 없는 번호 개수
    cnt_win = 0         # 맞춘 번호 개수
    
    for l in lottos:
        if l == 0:
            cnt_zero += 1
            continue
        if l in win_nums:
            cnt_win += 1
    
    return [ranking[cnt_zero + cnt_win], ranking[cnt_win]]