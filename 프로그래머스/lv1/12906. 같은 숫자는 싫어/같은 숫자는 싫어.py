def solution(arr):
    answer = []
    if arr:
        answer = [arr[0]]
        for a in range(1, len(arr)):
            if answer[-1] == arr[a]:
                continue
            else:
                answer.append(arr[a])
    return answer