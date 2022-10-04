code = input()
res = ''
for c in code:
    if c.isalpha():
        rot13 = ord(c) + 13
        if (c.islower() and 97 <= rot13 <= 122) or (c.isupper() and 65 <= rot13 <= 90):    # 아스키 코드로 소문자가 소문자, 대문자가 대문자로 변환되었다면 res에 추가
            res += chr(rot13)
        else:
            rot13 -= 26
            res += chr(rot13)

    else:              # 알파벳이 아닌 문자는 변환 없이 추가
            res += c
print(res)