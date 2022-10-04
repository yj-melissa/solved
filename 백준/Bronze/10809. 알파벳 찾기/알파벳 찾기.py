word = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
res = [-1] * len(alphabets)

for i in range(len(alphabets)):
    for j in range(len(word)):
        if alphabets[i] == word[j]:
            res[i] = j
            break

print(*res)
