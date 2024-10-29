import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) >= 2:
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville, f + s * 2)
        answer += 1
        
    if scoville[0] >= K:
        return answer
    return -1