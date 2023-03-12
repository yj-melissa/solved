def solution(brown, yellow):
    answer = []
    size = brown + yellow           # 카펫 총 칸 수는 brown + yellow
    for i in range(size, 1, -1):        # yellow가 1 이상이므로 col이 1 이상임. row가 더 크므로 역순으로 조회
        if size % i == 0:            # size의 약수일 때 검사
            row, col = i, (size // i)            
            if (row-2) * (col - 2) == yellow:
                answer = [row, col]
                break
    
    return answer