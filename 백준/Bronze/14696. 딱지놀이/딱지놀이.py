N = int(input())    # 라운드 수
for _ in range(N):
    A = list(map(int, input().split()))    # A[0]: 매 라운드 A가 낸 딱지 개수, 이후 A가 낸 딱지
    A_num = A[0]
    A = A[1:]
    B = list(map(int, input().split()))    # B[0]: 매 라운드 B가 낸 딱지 개수, 이후 B가 낸 딱지
    B_num = B[0]
    B = B[1:]

    # 별 개수 비교
    if A.count(4) > B.count(4):
        print('A')
        continue
    elif B.count(4) > A.count(4):
        print('B')
        continue
    # 동그라미 개수 비교
    else:
        if A.count(3) > B.count(3):
            print('A')
            continue
        elif B.count(3) > A.count(3):
            print('B')
            continue
        # 네모 개수 비교
        else:
            if A.count(2) > B.count(2):
                print('A')
                continue
            elif B.count(2) > A.count(2):
                print('B')
                continue
            # 세모 개수 비교
            else:
                if A.count(1) > B.count(1):
                    print('A')
                    continue
                elif B.count(1) > A.count(1):
                    print('B')
                    continue
                # 무승부
                else:
                    print('D')