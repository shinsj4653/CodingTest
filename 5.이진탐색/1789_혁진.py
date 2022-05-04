import sys
S = int(sys.stdin.readline())
check = 0
cnt = 1

while(True):
    if S<check:
        break
    else:
        check+=cnt
        cnt+=1

print(cnt-2)