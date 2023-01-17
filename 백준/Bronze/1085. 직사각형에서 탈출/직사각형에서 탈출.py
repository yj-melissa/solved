x, y, w, h = map(int, input().split())    # (x, y) = 현재 위치, (w, h) = 최대 위치

# x, y, (h-y), (w-x) 중 가장 작은 값이 경계선까지 가는 거리의 최솟값
distances = [x, y, (h-y), (w-x)]

min_distance = min(distances)     # 최소 거리
print(min_distance)

