def solution(sizes):
    max_w = max_h = 0       # 최대 가로, 최대 세로
    
    for size in sizes:
        size.sort()         
        w, h = size         # 길이 짧으면 가로, 길면 세로
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    answer = max_w * max_h
    return answer