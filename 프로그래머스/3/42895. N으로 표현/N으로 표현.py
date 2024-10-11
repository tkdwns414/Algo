def solution(N, number):
    dp = list(set([int(str(N) * i)]) for i in range(1,9))
    
    for i in range(8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        if number in dp[i]:
            return i + 1
                
    return -1

# 답을 참고해버린 문제
# dp를 단순히 해오던 방식으로만 사용하려하면 불가능한 문제인듯