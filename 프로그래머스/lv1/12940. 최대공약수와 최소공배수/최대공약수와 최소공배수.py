def solution(n, m):
    answer = [0, 0]
    if n > m:
        n, m = m, n 
    
    # 최대공약수
    for i in range(m, 0, -1):      # 최대 공약수: n < m일 때 1 <= x <= m
        if n % i == 0 and m % i == 0:
            answer[0] = i
            break
    
    # 최소공배수
    for j in range(m, n*m+1):       # 최소 공배수: n < m일 때, m <= y <= n*m
        if j % n == 0 and j % m == 0:
            answer[1] = j
            break
        
    return answer