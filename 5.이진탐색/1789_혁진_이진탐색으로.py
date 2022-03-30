import sys
S = int(sys.stdin.readline())
ans = 0
left, right = 1, S

while left<=right:
    mid = (left+right)//2
    if mid*(mid+1)//2 <= S:
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(ans)