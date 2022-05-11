import sys
n = int(sys.stdin.readline())
ans = 0
for _ in range(n):
    flag = True
    in_str = sys.stdin.readline()
    for i in range(len(in_str)-2):
        if not flag:
            ans-=1
            break
        cnt = in_str.count(in_str[i], i)
        for j in range(1, cnt):
            if in_str[i] == in_str[i+j]:
                continue
            else:
                flag = False
                break
    ans+=1

print(ans)