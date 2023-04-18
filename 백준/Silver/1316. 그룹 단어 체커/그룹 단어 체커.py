N = int(input())
answer = N
for _ in range(N):
    word = input()
    cnt = []                    # 나온 알파벳 정리
    last_w = ''
    for w in word:
        if w not in cnt:        # 나온적 없는 알파벳이면 ㅇㅋ
            cnt.append(w)
            last_w = w
            continue
        if w == last_w:         # 앞서 나온 문자와 동일해도 ㅇㅋ
            continue
        answer -= 1
        break                   # 이미 나온적 있는데 앞의 문자와 다르다면 실패
print(answer)