import sys
lst = list(map(int, sys.stdin.readline().split()))

def clock_num(n):
    val = int(''.join(map(str, n)))
    for i in range(1, 4):
        check = int(''.join(map(str, n[i:] + n[:i])))
        val = min(val, check)
    return val

c_num = clock_num(lst)
count = 0
for i in range(1111, c_num+1):
    if '0' not in list(str(i)) and i == clock_num(list(map(int, str(i)))):
        count+=1
print(count)
