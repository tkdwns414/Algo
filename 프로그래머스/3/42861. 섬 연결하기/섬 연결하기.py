def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    dest = [i for i in range(n)]
    
    def find(n):
        if dest[n] != n:
            dest[n] = find(dest[n])
        return dest[n]
    
    def union(a, b):
        ap = find(a)
        bp = find(b)
        if ap < bp:
            dest[bp] = ap
        else:
            dest[ap] = bp
    
    for cost in costs:
        if find(cost[0]) != find(cost[1]): # 연결 안돼있어?
            union(cost[0], cost[1])
            answer += cost[2]
    
    return answer

# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 -> 최소 비용 return
# costs를 마지막 요소를 가지고 sort하기