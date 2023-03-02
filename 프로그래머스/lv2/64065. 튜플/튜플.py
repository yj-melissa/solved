def solution(string):
    answer = []
    string = string[2:-2].split('},{')      # 대괄호 삭제
    # 원소 갯수 기준 정렬
    for i in range(len(string)):
        for j in range(i, len(string)):
            if len(string[i]) > len(string[j]):
                string[i], string[j] = string[j], string[i]
    # 튜플화
    for s in string:
        s = list(map(int, s.split(',')))
        for num in s:
            if num not in answer:
                answer.append(num)
            
    return answer