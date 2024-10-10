def solve():

    def track(n, selected, nums, used):
        max_ans = 0
        if len(selected) == n:
            ans = 0
            for i in range(n-1):
                ans += abs(selected[i] - selected[i+1])
            return ans
        
        for i in range(n):
            if not used[i]:
                used[i] = 1; selected.append(nums[i])
                max_ans = max(max_ans, track(n, selected, nums, used))
                used[i] = 0; selected.pop()
        return max_ans

    n = int(input())
    nums = list(map(int, input().split()))
    print(track(n, [], nums, [0] * n))

    
solve()

# 21:12 시작
# 21:40 제출
# abs를 크게 하려면 양수 - 음수가 많을 수록 좋음
# 그냥 줄 세우고 양 끝끼리 빼서 더하면 될듯 -> 문제 이해 잘못함
# 어떻게 해야지 가장 큰 값이 나오는지 모르겠음 -> 일단 완탐으로 돌려
# 근데 완탐을 어떻게 하지?
# 순서 고르고 순서 다 고르면 그 다음에 계산 ㄱㄱ