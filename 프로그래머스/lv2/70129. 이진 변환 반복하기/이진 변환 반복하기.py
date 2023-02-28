def solution(s):
    answer = [0, 0]  # answer = [(변환 횟수), (제거한 0 갯수)]

    while s != "1":
        answer[1] += s.count('0')  # 0 갯수 추가
        s = str(bin(s.count('1')))[2:]  # 1의 갯수를 2진수로 변환 / '0b' 제거 위해 슬라이싱
        answer[0] += 1  # 변환 횟수 추가

    return answer
