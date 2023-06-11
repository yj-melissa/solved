def solution(elements):
    len_e = len(elements)
    sums = set()        # 합한 수
    
    for i in range(1, len_e+1):  # 길이가 i인 연속 부분 수열 확인
        for s in range(len_e):   # s = 부분수열 시작점
            e = s + i           # end = 부분수열 종료점
            if e > len_e:    # 리스트 범위 벗어났을 때 시작점으로 되돌림
                e -= len_e
            partial = elements[s:e] if s < e else elements[:e] + elements[s:]   # 부분수열 확인
            sums.add(sum(partial))
    
    return len(sums)