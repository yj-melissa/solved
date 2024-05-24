def str_to_set(str):    
    tmp_set = []
    
    str = str.lower()
    for i in range(len(str)-1):
        sliced = str[i : i + 2]
        if not sliced.isalpha():        # 알파벳만 남김
            continue
        tmp_set.append(sliced)
    
    return tmp_set
    
    

def solution(str1, str2):    
    answer = 0
    
    set1 = str_to_set(str1)
    set2 = str_to_set(str2)
    
    union = 0       # 합집합
    inter = 0       # 교집합
    
    for a in set1:
        if a in set2:
            union += 1
            inter += 1
            set2[set2.index(a)] = 0
        else:
            union += 1
    
    union += len(set2) - set2.count(0)
    
    if union == 0:
        answer = 65536
        
    else:
        answer = int((inter / union) * 65536)
    
    return answer