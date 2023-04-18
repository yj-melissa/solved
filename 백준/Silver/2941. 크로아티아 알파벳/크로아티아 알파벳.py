cro_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']        # 알파벳 리스트
word = str(input())
for alpha in cro_alphabet:
    while alpha in word:                   # 크로아티아 알파벳이 포함되어 있다면 임의의 문자로 대체
        word = word[:word.find(alpha)] + '0' + word[word.find(alpha)+len(alpha):]
print(len(word))