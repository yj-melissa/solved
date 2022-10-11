T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 학생 수
    info = [sorted(list(map(int, input().split()))) for _ in range(N)]    # 방 정보
    rooms = [0] * 201    # 방 1~400번까지 있음 -> 복도는 200개

    for i in range(N):
        f = (info[i][0] + 1) // 2
        t = (info[i][1] + 1) // 2
        for j in range(f, t+1):
            rooms[j] += 1
            
    cnt = max(rooms)

    print(f'#{tc} {cnt}')