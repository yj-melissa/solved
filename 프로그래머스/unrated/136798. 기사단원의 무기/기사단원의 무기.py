def solution(number, limit, power):
    numbers = [2] * (number + 1)            # 초기화 : 기본적으로 1과 자기 자신을 약수로 가짐
    
    for n in range(2, number + 1):
        # 약수 갯수가 limit을 초과했다면 power로 조정
        if numbers[n] > limit:
            numbers[n] = power       
        # n의 배수에 약수 개수 추가
        m = 2
        while (n * m) <= number :
            numbers[n * m] += 1
            m += 1
    
    return sum(numbers[2:]) + 1