def solution(n):
    cnt = 0    # 3진법 자리수 확인
    for i in range(n):
        if n < 3 ** i:
            cnt = i - 1
            break
            
    tri = ''        # 3진법으로 변환한 수
    # 3진법으로 변환
    while n > 0:
        squared = 3 ** cnt
        
        if n >= 2 * squared :
            tri = '2' + tri
            n -= 2 * squared
            
        elif n >= squared :
            tri = '1' + tri
            n -= squared
            
        else:
            tri = '0' + tri
        cnt -= 1        
    
    answer = int(tri, 3)        # 10진법으로 변환
        
    return answer