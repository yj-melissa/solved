word1 = input()
word2 = input()
cnt = [0] * 26
answer = 0

for char in word1:
    idx = ord(char) - ord('a')
    cnt[idx] += 1

for char in word2:
    idx = ord(char) - ord('a')
    cnt[idx] -= 1

for c in cnt:
    answer += abs(c)

print(answer)