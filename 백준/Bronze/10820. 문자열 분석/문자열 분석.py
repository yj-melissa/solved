while input:
    try:
        strings = input()
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        cnt = [0, 0, 0, 0]    # 소문자, 대문자, 숫자, 공백 개수
        for s in strings:
            if s in lower:     # 소문자
                cnt[0] += 1
            elif s in upper:   # 대문자
                cnt[1] += 1
            elif s in nums:    # 숫자
                cnt[2] += 1
            else:              # 공백 개수
                cnt[3] += 1
        print(*cnt)
    except:
        break
