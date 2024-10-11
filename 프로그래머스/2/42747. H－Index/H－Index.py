def solution(citations):
    max_h = 0    
    for h in range(1, 10001):
        check = [citation >= h for citation in citations]
        if check.count(True) >= h and check.count(False) <= h:
            max_h = max(max_h, h)
        
    
    return max_h

# n편 중 h 번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다