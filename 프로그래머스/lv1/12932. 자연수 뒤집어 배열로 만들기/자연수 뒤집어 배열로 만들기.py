def solution(n):
    reversed_n = str(n)[::-1]       # 정수 n을 문자열로 변환, 역순으로 정렬
    answer = []
    for r in reversed_n:            # 역순으로 정렬했던 String 상태의 n을 하나씩 불러옴
        answer += [int(r)]          # int로 재변환해서 더함
    return answer