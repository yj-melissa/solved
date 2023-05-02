N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

coordinates.sort()
coordinates.sort(key=lambda x: x[1])

for c in coordinates:
    print(*c)