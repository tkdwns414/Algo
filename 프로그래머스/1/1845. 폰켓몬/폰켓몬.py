def solution(nums):
    nums_set = set(nums)
    n = len(nums)
    k = n // 2
    
    return min(k, len(nums_set))