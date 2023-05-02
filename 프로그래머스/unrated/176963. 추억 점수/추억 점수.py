def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        total = 0           # 사진의 추억점수
        for n in p:         # 사진에 있는 인물 순서대로 확인
            if n in name:
                total += yearning[name.index(n)]    # 추억 점수 추가
        answer.append(total)
    return answer