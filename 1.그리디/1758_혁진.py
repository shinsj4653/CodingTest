import sys
N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort(reverse=True)
ans = 0
for i in range(N):
    if lst[i]-i <0:
        continue
    else:
        ans += lst[i]-i

print(ans)