def solution(board, moves):
    answer = 0
    stack = []      # 뽑은 인형
    size = len(board)
    top = -1
    
    
    for m in moves:        
        doll = 0
        for r in range(size): # 인형 뽑기
            if board[r][m-1] == 0:
                continue
            doll = board[r][m-1]
            board[r][m-1] = 0       # 빈 공간으로 만듦
            break
        
        if doll == 0:               # 뽑을 인형이 없으면 넘어감
            continue
        
        if top > -1 and doll == stack[top]:      # 이전 인형과 같으면
            stack.pop()
            answer += 2
            top -= 1
            continue
        
        stack.append(doll)
        top += 1
    
    
    return answer