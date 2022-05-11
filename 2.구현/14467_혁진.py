import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = defaultdict(list)             #딕셔너리의 value를 list로 생성
ans = 0

for _ in range(N):
    key, value = map(int, sys.stdin.readline().split())
    if key in dic and dic[key][-1] != value:        #만약, 생성되있는 딕셔너리의 key값이 입력받은 key값과 같고 해당 key의 value의 마지막값이 입력받은 value와 다르면 +1
        ans+=1                                      #ex) 처음 (3,0)이 들어올 경우 else문을 이용해 dic에 해당 key와 value값 추가
        dic[key].append(value)                      #   그후 (3,1)이 들어오면 3은 이미 등록되어있는 key이고 1은 미리 들어온 value값인 0 과 다른 값을 가지므로 답+1
    else:
        dic[key].append(value)

print(ans)


