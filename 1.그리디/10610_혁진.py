import sys
N = list(sys.stdin.readline().rstrip())
check = 0
for i in range(len(N)):
    check += int(N[i])
N.sort(reverse=True)

if check % 3 ==0 and '0' in N:
    print(''.join(N))
else:
    print(-1)