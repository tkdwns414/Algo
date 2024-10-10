def solve():

    def track(n, m, nums, last):
        if m == len(nums):
            print(" ".join(map(str, nums)))
            return
        
        for i in range(last, n):
            nums.append(i + 1)
            track(n, m, nums, i)
            nums.pop()
    
    n, m = map(int, input().split())
    track(n, m, [], 0)
    
solve()

# 21:04 시작
# 21:06 제출