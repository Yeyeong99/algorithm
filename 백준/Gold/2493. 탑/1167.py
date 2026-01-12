v = int(input())
nodes = [[] for _ in range(v + 1)]
for i in range(v):
    line = list(map(int, input().split()))
    idx = line[0]
    infos = line[1: -1]
    for j in range(len(infos)):
        if j % 2 == 0:
            nodes[idx].append((infos[j], infos[j + 1]))

def sorted_(node):
    return sorted(node, key=lambda x: x[-1], reverse=True)
nodes = list(map(sorted_, nodes))

visited = [0] * (v + 1)
max_len = 0

def dfs(idx, length):
    global visited, max_len
    if visited[idx]:
        return

    for i in range(len(nodes[idx])):
        if max_len < length:
            max_len = length

        nxt_idx, nxt_len = nodes[idx][i][0], nodes[idx][i][1]

        visited[idx] = 1
        length += nxt_len
        dfs(nxt_idx, length)
        visited[idx] = 0
        length -= nxt_len

dfs(1, 0)

print(max_len)
