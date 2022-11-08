def ordering():
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]


N = int(input())
nums = [int(input()) for _ in range(N)]
ordering()
for i in range(N):
    print(nums[i])
