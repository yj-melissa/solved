N = int(input())
Q = [0] * 1000000
front = rear = -1

# 카드 삽입
for n in range(1, N+1):
    rear += 1
    Q[rear] = n

while rear - front > 1:
    # 제일 앞 카드 버림
    front += 1
    Q[front] = 0

    # 카드 옮김
    front += 1
    rear += 1
    Q[rear] = Q[front]
    Q[front] = 0
print(Q[rear])