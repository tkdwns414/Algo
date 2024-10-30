import heapq

def solution(jobs):
    answer = 0
    last = -1
    time = 0
    cnt = 0
    
    heap = []  
    
    while cnt < len(jobs):
        for job in jobs:
            if last < job[0] <= time:
                heapq.heappush(heap, (job[1], job[0]))
        
        if heap:
            j = heapq.heappop(heap)
            last = time
            time += j[0]
            answer += time - j[1]
            cnt += 1
        else:    
            time += 1
            
    return answer // cnt

## 도착한 시간이 작은(빠른)순, 작업 시간이 짧은 순으로 정렬
## 현재 시간 기준, 지금 작업할 수 있는 애들 중 가장 짧게 걸리는 애
## 현재 시간보다 작은 애들 중 가장 빠른 애를 찾기
## 여러개 있을 때 하나 끝나면 또 짧은 애가 새로 들어왔을 수도 있음에 주의
## last = time을 time에 새 값을 하기 전에 해줘야 함