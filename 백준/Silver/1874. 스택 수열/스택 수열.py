N = int(input())
nums = [int(input()) for _ in range(N)]
stack = [0] * 100001
top = -1
n = 1    # 스택에 마지막으로 저장한 숫자
res = []    # 결과값 저장할 리스트
for i in range(N):
    while n <= nums[i]:    # 오름차순으로 스택에 넣으므로 num[i]만큼 들어갈 때까지 push
        top += 1
        stack[top] = n
        n += 1
        res.append('+')
    if stack[top] == nums[i]:    # 스택 top과 출력해야할 숫자가 같다면 팝
        top -= 1
        res.append('-')
    elif nums[i] < stack[top]:    # 팝해야 할 숫자보다 스택 top 숫자가 더 낮다면 실패
        print('NO')
        break
else:
    for j in range(len(res)):
        print(res[j])