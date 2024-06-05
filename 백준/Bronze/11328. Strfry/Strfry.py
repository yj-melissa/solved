N = int(input())
for _ in range(N):
    tc = list(input().split())
    length = len(tc[0])
    cnt = [0] * 26          # 알파벳 카운팅 리스트

    for char in tc[0]:
        first = ord(char) - ord('a')
        cnt[first] += 1
        
    for char in tc[1]:
        second = ord(char) - ord('a')
        cnt[second] -= 1

    answer = "Possible"

    for c in cnt:
        if c != 0:
            answer = "Impossible"
            break

    print(answer)