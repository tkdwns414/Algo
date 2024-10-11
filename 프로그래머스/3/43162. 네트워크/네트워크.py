def solution(n, computers):
    visited = [0] * n
    network = 1

    def dfs(node, network):
        stack = []
        stack.append(node)
        
        while stack:
            cur = stack.pop()
            visited[cur] = network
            for i in range(n):
                if computers[cur][i] and not visited[i]:
                    stack.append(i)
                
        
    for i in range(n):
        if not visited[i]:
            dfs(i, network)
            network += 1
            
    
    return network - 1
