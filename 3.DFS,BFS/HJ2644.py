import sys
sys.setrecursionlimit(300000)

n = int(sys.stdin.readline())
fir, sec = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] *(n+1)
m = int(sys.stdin.readline())

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(graph, v, level):
    level +=1
    visited[v] = 1
    print(v, level)
    if v == sec:
       print(level-1)
       exit()

    for i in range(1, n+1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, level)

dfs(graph, fir, 0)
print(-1)

