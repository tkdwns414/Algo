from collections import Counter

def solution(cards):
    answer = 0
    
    def solve(start: int, visited: list, group: int):
        cur = start
        while visited[cur] == 0:
            visited[cur] = group
            cur = cards[cur] - 1
            
        card_cnt = Counter(visited)
        return card_cnt.get(group, 0), visited
    
    for i in range(len(cards)):
        first = 0; second = 0
        visited = [0] * len(cards)
        
        first, visited = solve(i, visited, 1)
        for j in range(len(cards)):
            second_visited = visited.copy()
            if second_visited[j] == 0:
                second, _ = solve(j, second_visited, 2)
                answer = max(answer, first*second)
    return answer

# 상자 안과 상자에 붙은 번호는 다름
# 상자 하나 열고 그 상자 안에 있는 카드 숫자를 확인함
# 카드 숫자에 해당하는 상자를 열음
# 열어야 하는 상자가 이미 있는 열려있다면 그때 1 번 상자 그룹임
# 한 번 더 돌려서 멈추면 그게 2번 상자 그룹임
# 그리고 그 점수가 최대가 돼야 함
# -> 뭐를 처음 뽑았을지 모두 확인해야할듯?