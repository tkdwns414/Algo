def solution(n, computers):
    visited = [0] * n
    network_num = 1

    def dfs(net, visited, node):
        stack = [node]
        while stack:
            cur_node = stack.pop()
            for i in range(n):
                if computers[cur_node][i] == 1 and visited[i] == 0:
                    visited[i] = net
                    stack.append(i)
                    
    for i in range(n):
        if visited[i] == 0: # 방문하지 않은 곳(네트워크가 형성되지 않은 곳)
            dfs(network_num, visited, i)
            network_num += 1
            
    print(visited)
    
    return max(visited)


# 0부터 n-1까지 돌아가면서 visited가 아닐 때 dfs를 실행
