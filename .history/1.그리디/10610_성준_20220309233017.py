n = list(input())
n.sort(reverse=True)

answer = -1

newList = []

index = 0
for num in n :
  if index > 2 and int(num) == 0 :
    break
  
  else :
    newList.append(int(num))
    index += 1

listlen = len(newList) - 1
finalNum = 0

for num in newList :
  finalNum += num * (10 ** listlen)
  listlen -= 1

if finalNum % 30 == 0:
  print(finalNum)
  
else :
  print(-1)

#print(numList)

