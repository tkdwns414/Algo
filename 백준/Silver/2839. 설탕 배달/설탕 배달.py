def solve():
    n = int(input())
    ans = 0
    while n > 0:
        if n % 5 == 0:
            ans += n // 5 
            n = n % 5
        else:
            n -= 3
            ans += 1 
    if n < 0:
        print(-1)
    else:
        print(ans)

solve()