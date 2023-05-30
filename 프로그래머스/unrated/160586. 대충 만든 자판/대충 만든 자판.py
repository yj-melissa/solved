def solution(keymap, targets):
    answer = []
    
    # 1. 입력할 문자열 targets 순서대로 순회
    for target in targets:
        total = 0               # 문자열 입력에 필요한 횟수
    # 2. target의 문자 t 순회
        for t in target:
    # 3. target을 입력하려면 keymap 최소 몇 번 눌러야 하는지 확인
            cnts = []
    # 3.1 각 keymap에서 입력 횟수 : idx + 1 (없는 경우 idx = -1임. 주의)
            for k in keymap:
                cnt = k.find(t) + 1
                if cnt == 0:
                    continue
                cnts.append(cnt)
    # 4. target 최소 입력 횟수 total에 추가   
    # 4.1 입력할 수 없는 경우 -1을 answer에 추가하고 다음 문자열 검사
            if len(cnts) == 0:
                total = -1
                break
            else:
                total += min(cnts)
    # 5. targets 순회가 끝났다면 answer에 total 추가
        answer.append(total)
    
    
    
    
    return answer