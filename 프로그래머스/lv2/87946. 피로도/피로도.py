from itertools import permutations

def solution(k, dungeons):
    dungeons.sort(reverse=True)     # 최소 필요도가 큰 순으로 정렬
    
    for i in range(len(dungeons), 0, -1):
        orders = list(permutations(dungeons, i))        # 차례로 던전 도는 조합
        print(i)
        for order in orders:
            stamina = k
            for min_stamina, use_stamina in order:
                if stamina >= min_stamina:       # 최소 필요 피로도 넘으면 탐험
                    stamina -= use_stamina
                else:
                    break
            else:           # 던전 도는 데 성공했으면 i 반환
                return i           
    
    
    return 0