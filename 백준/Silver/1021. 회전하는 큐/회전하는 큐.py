from collections import deque

def move_left():
    temp = queue.popleft()
    queue.append(temp)

def move_right():
    temp = queue.pop()
    queue.appendleft(temp)

# 1021 회전하는 큐
N, M = map(int, input().split())        # N : 크기, M : 뽑아낼 수
m_list = list(map(int, input().split()))
queue = deque(x for x in range(1, N+1))
cnt = 0

for m in m_list:
    idx = queue.index(m)    # 현재 뽑아낼 수의 위치 확인
    times = idx if idx < (N-idx) else N-idx     # 왼쪽, 오른쪽 더 가까운 쪽으로 선택
    direction = 0 if idx == times else 1           # 0 왼쪽 1 오른쪽

    while times > 0:        # m이 제일 왼쪽에 올 때까지 반복
        if direction:
            move_right()
        else:
            move_left()
        times -= 1
        cnt += 1

    # 뽑을 수가 0번 인덱스로 왔다면 pop
    queue.popleft()
    N -= 1
    continue

print(cnt)

