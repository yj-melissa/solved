def find_idx(alphabet):
    vowel = ["A", "E", "I", "O", "U"]
    
    for i in range(5):
        if alphabet == vowel[i]:
            return i

def solution(word):
    answer = 0
    # 단어 위치 증가 규칙
    fifth = (5 ** 0)
    fourth = (5 ** 1) + fifth
    third = (5 ** 2) + fourth
    second = (5 ** 3) + third
    first = (5 ** 4) + second
    
    increased = [first, second, third, fourth, fifth]
    
    
    for i in range(len(word)-1, -1, -1):
        apb_idx = find_idx(word[i])
        answer += increased[i] * apb_idx + 1    
    
    return answer