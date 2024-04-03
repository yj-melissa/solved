import sys

def binary_search(arr, target):
    s = 0
    e = len(arr) - 1
    answer = 0

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return 0


N = int(input())
x_list = list(map(int, sys.stdin.readline().rstrip().split()))
coords = list(set(x_list))      # 중복 좌표 제거
coords.sort()

for i in range(N):
    print(binary_search(coords, x_list[i]), end = ' ')