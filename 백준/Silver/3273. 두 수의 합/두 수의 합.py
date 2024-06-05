n = int(input())
nums = list(map(int, input().split()))
x = int(input())

answer = 0

nums.sort()
left = 0
right = n - 1

while left < right:
    added = nums[left] + nums[right]
    if added == x:
        answer += 1
        left += 1
        right -= 1
    elif added < x:
        left += 1
    else:
        right -= 1

print(answer)