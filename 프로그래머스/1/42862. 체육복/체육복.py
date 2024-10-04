def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    
    new_reserve.sort()
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
    
    return n - len(new_lost)

## 가장 많이 빌리는 방법은? -> 그냥 작은 애부터 빌릴 수 있으면 쭉 빌리는 것
## 실제 잃어버리고 여분이 있는 애들만 남기기 (여분 가져온 애도 도난 됐을 수 있음)