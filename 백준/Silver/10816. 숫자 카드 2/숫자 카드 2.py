cards_minus = [0] * 10000001
cards_plus = [0] * 10000001

N = int(input())        # 상근이가 가지고 있는 카드 갯수
cards = list(map(int, input().split()))      # 상근이가 가진 카드 목록
for c in cards:
    if c >= 0:
        cards_plus[c] += 1
    else:
        cards_minus[-c] += 1

M = int(input())        # 찾아야할 카드 갯수
find_cards = list(map(int, input().split()))        # 찾아야할 카드 목록

for f in find_cards:
    if f >= 0:
        print(cards_plus[f], end=' ')
    else:
        print(cards_minus[-f], end=' ')
