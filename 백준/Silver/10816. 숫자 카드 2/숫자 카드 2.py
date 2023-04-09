N = int(input())        # 상근이가 가지고 있는 카드 갯수
have_cards = list(map(int, input().split()))        # 상근이가 가진 카드 목록
card_dict = dict()

for c in have_cards:
    if c in card_dict:
        card_dict[c] += 1
    else:
        card_dict[c] = 1

M = int(input())        # 찾아야할 카드 갯수
find_cards = list(map(int, input().split()))        # 찾아야할 카드 목록

for f in find_cards:
    if f in card_dict:
        print(card_dict[f], end=' ')
    else:
        print(0, end= ' ' )