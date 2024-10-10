def solve():

    def track(n, m, nums, visited):
        if m == len(nums):
            print(" ".join(map(str, nums)))
            return
        
        for i in range(n):
            if not visited[i]:
                visited[i] = 1; nums.append(i + 1)
                track(n, m, nums, visited)
                visited[i] = 0; nums.pop()
    
    n, m = map(int, input().split())
    track(n, m, [], [0] * n)
    
solve()

# 20:51 시작
# 20:58 제출