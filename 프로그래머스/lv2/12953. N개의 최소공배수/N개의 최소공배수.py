def solution(arr):
    n = max(arr)
    i = 1
    answer = -1
    
    while answer == -1:
        for a in arr:
            if (n * i) % a:
                i += 1
                break
        else:
            answer = n * i
    return answer
            