import sys

# 백준 9093: 단어 뒤집기

T = int(input())        # 테스트 케이스 수 T
for t in range(T):      # 테스트 케이스 수만큼 반복
    word_list = input().split()      # 공백 기준으로 분할 -> 리스트에 저장
    sentence = ''       # 뒤집은 문장

    for word in word_list:     # 리스트에 있는 단어 하나씩 꺼내서 사용
        sentence += word[::-1]  # 단어를 뒤집어 sentence에 추가
        sentence += ' '         # 단어 뒤에 공백 추가

    print(sentence)