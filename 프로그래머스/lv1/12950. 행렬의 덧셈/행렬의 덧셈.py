def solution(arr1, arr2):
    arr_len = len(arr1)
    answer = [0] * arr_len
    
    for r in range(arr_len):
        a1, a2 = arr1[r], arr2[r]
        a1_len = len(a1)
        answer[r] = [0] * a1_len
        for c in range(a1_len):
            answer[r][c] = a1[c] + a2[c]
        
    return answer