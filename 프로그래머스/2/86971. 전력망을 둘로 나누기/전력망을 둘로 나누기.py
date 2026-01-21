def solution(n, wires):
    graph = {}
    for i in range(len(wires)):
        graph.setdefault(wires[i][0], []).append(wires[i][1])
        graph.setdefault(wires[i][1], []).append(wires[i][0])
    
    def dfs(k):
        nonlocal min_diff
        nonlocal num
        num += 1

        for key in graph[k]:
            if visited[key]:
                continue
            visited[key] = 1
            dfs(key)
            visited[key] = 0
            
    min_diff = float('inf')
    for key in graph:
        visited = [0] * (n + 1)
        visited[1] = 1
        visited[key] = 1
        num = 0
        
        dfs(1)
        
        diff = abs(num - (n - num))
        if diff < min_diff:
            min_diff = diff
            
    return min_diff