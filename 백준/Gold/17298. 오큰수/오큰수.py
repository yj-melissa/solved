import sys
N = int(input())    # 리스트 크기
A = list(map(int, sys.stdin.readline().split()))
NGE = [-1] * N     # 정답값 모을 리스트. -1 : 오큰수 없을 때 출력해야하므로 초기화값으로 설정
stack = [0] * N    # A 리스트 인덱스 저장할 리스트.
top = 0

for i in range(1, N):
    while top > -1 and A[stack[top]] < A[i]:    # 스택이 비어있지 않고 A[stack[top]]이 A[i]보다 작으면
        NGE[stack[top]] = A[i]               # top 인덱스의 NGE는 A[i]
        top -= 1
    top += 1
    stack[top] = i                           # 오큰수 찾아야 할 인덱스 스택에 추가

print(*NGE)