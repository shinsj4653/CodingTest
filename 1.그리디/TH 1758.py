# 원래 주려고 생각했던 돈 - 받은등수 +1
# 민호1 재필2 주현3
# 3-1+1 2-2+1 1-3+1 3 1 -1
# 받을 수 있는 팁의 최댓값
N = int(input())
answer=0
tip=[]
for i in range(N):
    tip.append(int(input()))
tip.sort(reverse=True)
for i in range(N):
    temp = tip[i]-i
    if temp>=0:
        answer+=temp
print(answer)
#깎일 건 정해져 있으니까