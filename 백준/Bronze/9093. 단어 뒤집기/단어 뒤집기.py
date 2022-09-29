T = int(input())
for _ in range(T):
    string = list(input().split())    # 문장 띄어쓰기 기준으로 나누어 리스트에 삽입
    reverse = []    # 뒤집은 문자열 추가할 리스트
    for i in range(len(string)):
        r = string[i][::-1]    # 역순으로 슬라이싱
        reverse.append(r)
    print(*reverse)