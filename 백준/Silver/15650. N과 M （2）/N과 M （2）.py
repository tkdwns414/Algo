def solve():

    def track(n, m, nums, visited, last):
        if m == len(nums):
            print(" ".join(map(str, nums)))
            return
        
        for i in range(last + 1, n):
            if not visited[i]:
                visited[i] = 1; nums.append(i + 1)
                track(n, m, nums, visited, i)
                visited[i] = 0; nums.pop()
    
    n, m = map(int, input().split())
    track(n, m, [], [0] * n, -1)
    
solve()

# 21:00 시작
# 21:02 제출