def solve():
    n, k = map(int, input().split())
    nums = input()
    stack = []
    cnt = 0

    for i, num in enumerate(nums):
        while stack and stack[-1] < nums[i] and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(num)
    
    if len(stack) != n - k:
        for _ in range(len(stack) - (n - k)):
            stack.pop()
    
    print("".join(stack))

    
solve()

# 20:12 시작
# 20:33 제출
# 앞에부터 현재 수보다 작으면 뱉기를 k번
# https://www.acmicpc.net/board/view/147182
# 수가 같아서 마지막에 숫자가 남으면 그때도 해줘야 함