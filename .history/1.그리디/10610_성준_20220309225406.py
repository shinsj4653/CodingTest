n = input()
numList = []
index = 0
for num in n :
  if index > 2 :
    if int(num) == 0 :
      break
    else :
      numList.append(int(num))
      index += 1

numList.sort(reverse=True)

listlen = numList.length() - 1
finalNum = 0

for num in numList :
  finalNum += num * (10 ** listlen)
  listlen -= 1

#print(numList)

