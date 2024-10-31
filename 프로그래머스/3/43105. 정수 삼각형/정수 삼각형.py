def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left = triangle[i - 1][j - 1] if j > 0 else 0
            right = triangle[i - 1][j] if j < len(triangle[i - 1]) else 0
            triangle[i][j] += max(left, right)
    
    return max(triangle[-1])

# 거쳐간 숫자의 최댓값을 return하도록
# 한 층씩 확인을 하는데
    # 본인의 인덱스가 idx라면
    # idx, idx + 1만 확인 (있을 때만 확인)
    # 더 큰 값을 본인에게 더하기
    # 마지막 중 max 반환