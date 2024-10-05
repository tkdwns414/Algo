def solve():
    t = int(input())

    dp = [[-1] * 30 for _ in range(30)]

    for i in range(30):
        for j in range(30):
            if i == 0:
                dp[i][j] = j + 1
            elif i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = sum(dp[i-1][i-1:j])

    for _ in range(t):
        n, m = map(int, input().split())
        print(dp[n-1][m-1])
    
   

solve()
# 시간제한 0.5초
# 18:20
# 18:48