import sys

input = sys.stdin.readline

while True:
    tc = input().strip()

    if tc == "0":     # 테스트케이스 종료
        break

    graphs = list(map(int, tc.split()))
    n = graphs[0]
    graphs = graphs[1:]
    stack = []      # (idx, height)
    answer = 0

    for i in range(n):
        start = i
        while stack and stack[-1][1] > graphs[i]:      # 새로 나온 막대가 더 짧으면 넓이 비교
            idx, height = stack.pop()
            answer = max(answer, height * (i - idx))
            start = idx
        stack.append((start, graphs[i]))

    while stack:
        idx, height = stack.pop()
        answer = max(answer, height * (n - idx))

    print(answer)