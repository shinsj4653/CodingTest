import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
check_lst = []

for i in range(N):
    check_lst.append((lst[i], i))   #각 index와 그 index에 해당되는 값을 저장한 check_lst생성

check_lst.sort()                    #check_lst를 해당 값에 따라 정렬
count = 0
for i in range(N):
    if not i:                       #check_lst의 index가 0일때(값이 가장 작을때)
        lst[check_lst[i][1]] = count
        count+=1
    else:
        if check_lst[i][0] == check_lst[i-1][0]:        #이전 값과 값이 같다면 count증가된 값에서 1만큼 빼고 count동결
            lst[check_lst[i][1]] = count-1
        else:                                           #이전 값과 값이 다르다면 count를 해당 index의 lst에 저장하고 count+1
            lst[check_lst[i][1]] = count
            count+=1

print(*lst)
