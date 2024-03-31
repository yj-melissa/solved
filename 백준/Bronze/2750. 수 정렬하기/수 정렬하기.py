import sys
sys.setrecursionlimit(10**6)

def quick_sort(start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and nums[left] <= nums[pivot]:
            left += 1
        while right > start and nums[right] >= nums[pivot]:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
        else:
            nums[start], nums[right] = nums[right], nums[start]

    quick_sort(start, right - 1)
    quick_sort(right + 1, end)

N = int(input())
nums = [0] * N

for i in range(N):              # 수 입력
    nums[i] = int(input())

quick_sort(0, N - 1)

for i in range(N):
    print(nums[i])