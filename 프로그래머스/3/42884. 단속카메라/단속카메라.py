def solution(routes):
    routes.sort()
    current = 0
    temp = routes[0]
    answer = 1 # 제일 기본 범위 하나 가지고 시작
    
    for idx, route in enumerate(routes):
        # 겹치는 부분이 있다면 겹치는 부분으로 temp를 업데이트
        # 겹치는 부분이 없다면 answer += 1 temp를 새 범위로
        if temp[0] <= route[0] <= temp[1]: # 정렬해서 앞에만 비교하면 됨
            temp[0] = max(temp[0], route[0])
            temp[1] = min(temp[1], route[1])
        else:
            temp = route
            answer += 1
        
    return answer

# 왜 굳이 지점에 음수가 존재하지??