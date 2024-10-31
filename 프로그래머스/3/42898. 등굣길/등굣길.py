def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    
    for puddle in puddles:
        dp[puddle[1] - 1][puddle[0] - 1] = -1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: # 집일 때
                dp[i][j] = 1
            elif dp[i][j] != -1: # 연못이 아닐 때
                top = dp[i-1][j] if dp[i-1][j] != -1 else 0
                left = dp[i][j-1] if dp[i][j-1] != -1 else 0
                dp[i][j] = (top + left) % 1000000007
    
    return dp[n - 1][m - 1]

# 이거 초등 수학 그 문제 아닌가?
# 왼쪽 방향에서 오는 방법 + 위쪽 방향에서 오는 방법 = 그 방향으로 가는 총 방법