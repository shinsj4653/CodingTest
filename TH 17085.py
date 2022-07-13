n,m = map(int,input().split())
graph=[]
# 놓인 십자가 넓이의 곱의 최대값
for i in range(n):
    graph.append(list(input()))
# print(graph)
ans=[]
visited=[[0]*m for _ in range(n)]
# print(visited)
for i in range(n):
    for j in range(m):
        if graph[i][j]=='#':
            temp=0
            while -1<i-temp and i+temp<n and -1<j-temp and j+temp<m:
                temp+=1
            while temp:
                ans.append([temp,i,j])
                temp-=1
