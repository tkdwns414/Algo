def solution(tickets):
    tickets.sort(reverse=True)
    travel = ["ICN"]
    stack = []
    
    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            visited = [False] * len(tickets)
            visited[idx] = True
            stack.append((idx, ticket, visited))

    while stack:
        cidx, cpath, cvisited = stack.pop()
        
        if all(cvisited):
            return cpath
        
        for idx, ticket in enumerate(tickets):
            if not cvisited[idx] and cpath[-1] == ticket[0]:
                cvisited[idx] = True
                stack.append((idx, cpath + [ticket[1]], cvisited[::]))
                cvisited[idx] = False
                
    return []


# 처음에 좀 이상하게 한듯?