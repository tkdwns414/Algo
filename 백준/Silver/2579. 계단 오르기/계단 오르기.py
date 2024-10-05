def solve():
    N = int(input())
    stairs = [0] * 301
    dp = [[0,0] for _ in range(301)]

    for i in range(N):
        stairs[i + 1] = int(input())

    dp[1][0] = stairs[1]
    dp[2][0] = stairs[2]
    dp[2][1] = stairs[1] + stairs[2]

    for i in range(3, 301):
        dp[i][0] = max(dp[i-2][1], dp[i-2][0]) + stairs[i]
        dp[i][1] = dp[i-1][0] + stairs[i]

    print(max(dp[N]))
   
solve()
# 20:12
# 20:29