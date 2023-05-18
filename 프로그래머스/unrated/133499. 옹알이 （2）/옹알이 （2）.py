def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]       # 발음 가능
    answer = 0
    
    for b in babbling:
        for i in range(4):
            b = b.replace(possible[i], f"{i}")      # 발음 가능한 단어는 숫자로 변경
        if b.isdigit():     # 숫자만 남아있을 때
            b = str(b)
            f = b[0]
            for i in range(1, len(b)):
                if f != b[i]:
                    f = b[i]
                    continue
                break
            else:
                answer += 1
    
    return answer