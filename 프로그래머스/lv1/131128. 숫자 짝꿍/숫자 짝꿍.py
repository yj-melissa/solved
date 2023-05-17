def solution(X, Y):
    answer = ''
    XY = list(set(X) & set(Y))
    XY.sort(reverse=True)
    
    if len(XY) == 0:
        return '-1'
    
    for i in XY:
        answer += i * min(X.count(i), Y.count(i))
    
    return answer if answer[0] != '0' else '0'