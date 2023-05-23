def solution(new_id):    
    # 1단계 : 소문자 치환
    new_id = new_id.lower()
    print(new_id)
    
    # 2단계 : 소문자, 숫자, -, _, . 제외 전부 제거
    possible = ["-", "_", "."]
    id = ''
    for c in new_id:
        if c.isalpha():        # 알파벳 확인
            id += c
            continue
        if c.isdigit():      # 숫자 여부 확인
            id += c
            continue
        if c in possible:
            id += c
            continue
    new_id = id
    print(new_id)
    
    # 3단계 : 마침표 2번 이상 연속된 경우 한 개로 치환
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
        continue
    print(new_id)
    
    # 4단계 : 마침표가 처음이나 끝이면 제거
    if new_id and (new_id[0] == '.'):
        new_id = new_id[1:]
    if new_id and (new_id[-1] == '.'):
        new_id = new_id[:len(new_id)]
    print(new_id)
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    print(new_id)
    
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    print(new_id)
    
    return new_id