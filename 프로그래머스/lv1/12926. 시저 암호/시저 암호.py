def solution(string, n):
    answer = ''
    # print(ord('a'), ord('z'), ord('A'), ord('Z'))
    
    for s in string:
        s = ord(s)
        if 97 <= s <= 122:      # 소문자일 때
            s  = 97 + (s + n - 97) % 26
        elif 65 <= s <= 90:     # 대문자일 때 
            s  = 65 + (s + n - 65) % 26
        # if 97 <= s <= 122 or 65 <= s <= 90:
        #     print(s, n % 25)
        #     s = 97 + (s + n - 97) % 26
        #     print(s)
        answer += chr(s)
    return answer