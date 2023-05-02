def solution(nums):
    N = len(nums)/2
    nums = set(nums)
    return len(nums) if N > len(nums) else N