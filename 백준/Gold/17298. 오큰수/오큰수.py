def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    answer = [-1 for _ in range(n)]
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            answer[stack.pop()] = nums[i]
            
        stack.append(i)
    
    for ans in answer:
        print(ans, end= " ")

solve()

# 16:19 시작
# 16:35 제출
# n으로 돌아야 함
# 아직 답을 못 구한 인덱스를 넣어두고 원하는 거 나오면 그때 넣기
# 답 참고해버렸음