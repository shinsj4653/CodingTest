import sys
N = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().split()) for _ in range(N)]

lst.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(lst[i][0])