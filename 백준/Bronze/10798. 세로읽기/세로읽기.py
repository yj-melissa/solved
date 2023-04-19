arr = [input() for _ in range(5)]
alphabet_dict = {}              # 각 단어의 길이가 다르므로 자리수 기준 dictionary에 추가

for r in range(5):
    for c in range(len(arr[r])):
        if c in alphabet_dict:
            alphabet_dict[c] += arr[r][c]
            continue
        alphabet_dict[c] = arr[r][c]

answer = ''
for a in alphabet_dict:
    answer += alphabet_dict[a]
print(answer)