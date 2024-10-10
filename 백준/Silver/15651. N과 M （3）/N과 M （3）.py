def solve():

    def track(n, m, nums):
        if m == len(nums):
            print(" ".join(map(str, nums)))
            return
        
        for i in range(n):
            nums.append(i + 1)
            track(n, m, nums)
            nums.pop()
    
    n, m = map(int, input().split())
    track(n, m, [])
    
solve()

# 21:03 시작
# 21:04 제출