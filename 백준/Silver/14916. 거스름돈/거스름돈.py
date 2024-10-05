def solve():
    coin = [0] * 100001
    coin[2] = 1
    coin[5] = 1

    for i in range(4, 100001):
        if coin[i-2] != 0 and coin[i-5] != 0:
            coin[i] = min(coin[i-2], coin[i-5]) + 1
        elif coin[i-2] != 0:
            coin[i] = coin[i-2] + 1
        elif coin[i-5] != 0:
            coin[i] = coin[i-5] + 1  

    n = int(input())
    print(coin[n] if coin[n] != 0 else -1)
    
   
solve()
# 19:39
# 19:53