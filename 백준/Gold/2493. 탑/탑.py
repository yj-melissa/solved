N = int(input())
towers = list(map(int, input().split()))
stack = []

for i in range(N):
    while stack:
        j = stack.pop()
        if towers[i] <= towers[j]:      # 같거나 더 높은 타워 만남
            print(j + 1, end = ' ')
            stack.append(j)
            stack.append(i)
            break
    if not stack:
        print(0, end = ' ')     # 더 높은 타워 없었음
        stack.append(i)