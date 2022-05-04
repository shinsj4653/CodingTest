import sys
N, M = map(int, sys.stdin.readline().split())
check_lst = []

for _ in range(N):
    check_lst.append(list(map(str, sys.stdin.readline().split())))
    check_lst[-1][1] = int(check_lst[-1][1])

for _ in range(M):
    val = int(sys.stdin.readline())
    start, end = 0, N-1
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if check_lst[mid][1] >= val:
            end = mid -1
            ans = mid
        else:
            start = mid+1
    print(check_lst[ans][0])

