n = list(input())
answer = -1
max_num = sorted(n, reverse=True)
max_num = int(''.join(max_num))
if(max_num % 30) == 0 :
  answer = max_num
  
print(answer)

# 놀랍게도 그냥 30으로 나눠도 풀린다..

# newList = []

# index = 0
# for num in n :
#   if index > 2 and int(num) == 0 :
#     break
  
#   else :
#     newList.append(int(num))
#     index += 1

# listlen = len(newList) - 1
# finalNum = 0

# for num in newList :
#   finalNum += num * (10 ** listlen)
#   listlen -= 1

# if finalNum % 30 == 0:
#   print(finalNum)
  
# else :
#   print(-1)

#print(numList)

