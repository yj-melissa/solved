def make_map(n, arr):                       # 지도 만드는 함수
    map_list = []
    for a in arr:
        bin_a = bin(a)[2:]                  # 이진수로 변환, 0b 제거
        if len(bin_a) < n:                  # 길이가 n보다 작은 경우 길이 맞춰줌
            bin_a = '0' * (n-len(bin_a)) + bin_a
        map_list.append(bin_a)
    return map_list
    

def solution(n, arr1, arr2):
    answer = []
    
    # 지도 1, 2 확인
    # arr1, arr2 숫자 -> 2진수로 변환
    # 2진수 변환시 길이는 최대 n
    map1 = make_map(n, arr1)
    map2 = make_map(n, arr2)
    
    
    # 원본 지도 확인
    # arr1, arr2 둘 중 하나라도 벽("#")이면 전체 지도에서도 벽
    for row in range(n):
        origin = ""
        for col in range(n):
            if int(map1[row][col]) + int(map2[row][col]) > 0:    # 한 쪽이라도 벽이라면 벽
                origin += "#"
            else:
                origin += " "
        answer.append(origin)
    
    # 원본 지도 출력
    return answer