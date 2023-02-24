def solution(arr):
    length = len(arr)
    answer = []
    if length == 1:
        answer = [-1]
    else:
        min_num = min(arr)      # 제일 작은 수 확인
        flag = True            # 아직 제일 작은 수 제외 못함
        for n in range(length):
            if arr[n] == min_num and flag:       # 제일 작은 수 & 제거도 하기 전이라면 추가하지 않음
                continue
            answer += [arr[n]]
                
    return answer