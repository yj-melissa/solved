def solution(array, commands):
    answer = []
    
    for c in range(len(commands)):
        i, j, k = commands[c][0], commands[c][1], commands[c][2]
        i_array = array[i-1:j]      # 잘라낸 배열
        i_array.sort()              # 정렬
        answer.append(i_array[k-1])
        # print(i_array)
        
    return answer