def dfs(numbers, target, idx, total):
    global answer
    if idx == len(numbers) - 1:
        if total == target:
            answer += 1
        return
    idx += 1
    dfs(numbers, target, idx, total + numbers[idx])
    dfs(numbers, target, idx, total - numbers[idx])
    

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, numbers[0])
    dfs(numbers, target, 0, -numbers[0])
    return answer