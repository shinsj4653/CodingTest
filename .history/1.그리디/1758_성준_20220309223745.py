n = int(input())
tipList = []
for i in range(n) :
  tipList.append(int(input()))
  
tipList.sort(reverse=True) # 내림차순으로 정렬해야 최댓값 구하기 가능
print(tipList)

# tip = 0
# place = 1
# # 음수일때는 생각 x
# for money in tipList: 
#   if money - (place - 1) < 0 :
#     break
  
#   else :
#     tip += money - (place - 1)
#     place += 1

# print(tip)

# print(tipList)
