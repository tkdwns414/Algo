def solution(number, k):
    stack = []; cnt = 0
    
    for num in number:
        while stack and stack[-1] < num and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(num)
    
    while len(stack) > len(number) - k:
        stack.pop()
        
    answer = str(int(''.join(stack)))
    return answer

# 왜 어디서 본 적 있는 문제같지
# 왼쪽부터 시작해서. 내가 이 다음에 나올 애보다 작다? 다 빼버리기
# 다 같은 수일 때 아무것도 안 빼는 문제가 있을 수도 있는 것 같음