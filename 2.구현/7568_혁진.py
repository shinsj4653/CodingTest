import sys
n = int(sys.stdin.readline())
rank = [1 for _ in range(n)]
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(n-1):
    for j in range(i+1, n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank[i] +=1
        elif lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            rank[j]+=1
print(*rank)
