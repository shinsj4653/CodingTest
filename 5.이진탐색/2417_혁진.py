import math
import sys
N = int(sys.stdin.readline())

ans = 0
left = 1
right = N

while left<=right:
    mid = (left+right)//2
    if mid**2 < N:
        left = mid +1
    elif mid**2 == N:
        ans = mid
        break
    else:
        ans = mid
        right = mid -1

print(ans)