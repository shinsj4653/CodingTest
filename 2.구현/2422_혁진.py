import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
lst = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b= map(int, sys.stdin.readline().split())
    lst[a-1][b-1] = True
    lst[b-1][a-1] = True

ans = 0
for i in itertools.combinations(range(N), 3):
    if lst[i[0]][i[1]] or lst[i[0]][i[2]] or lst[i[1]][i[2]]:
        continue
    else:
        ans+=1
print(ans)
