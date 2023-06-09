def solution(arr1, arr2):
    len_row = len(arr1)
    len_col = len(arr2[0])
    answer = [[0] * len_col for _ in range(len_row)]
    
    for i in range(len_row):
        for j in range(len_col):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer