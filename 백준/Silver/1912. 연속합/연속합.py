def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    dp = [0] * n
    for i in range(n):
        dp[i] = max(nums[i], dp[i-1] + nums[i] if i >= 1 else nums[i])

    return max(dp)


print(solve())
