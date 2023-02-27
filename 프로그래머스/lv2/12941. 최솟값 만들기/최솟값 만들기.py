def solution(A,B):
    answer = 0
    
    # for _ in range(len(A)):
        # answer += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))       # 효율성 테스트 실패
        
    A.sort()
    B.sort(reverse = True)
    for a, b in zip(A, B):
        answer += a * b

    return answer