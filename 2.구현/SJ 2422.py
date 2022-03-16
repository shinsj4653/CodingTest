#from itertools import combinations

n, m = map(int, input().split())
iceCreamTree = [[] * (n + 1) for _ in range(n + 1)]
ans = 0

for i in range(m) :
    x, y = map(int, input().split())
    iceCreamTree[x].append(y)
    iceCreamTree[y].append(x)

# 내풀이 : 메모리초과 발생

# rowNum = 0
# for iceCreamRow in iceCreamTree :
#     if rowNum == 0 :
#         rowNum += 1
#         continue
    
#     iList = []
    
#     for num in range(1, n + 1) :
#         if num > rowNum and num not in iceCreamRow :
#             if len(iList) == 0 :
#                 iList.append(num)
#             else :    
#                 for a in iList :
#                     if num not in iceCreamTree[a] :
#                         iList.append(num)
                        
#     ans += len(list(combinations(iList, 2)))
#     rowNum += 1

# 인터넷 풀이
# 조합 대신, j, k 활용
# j -> i + 1 ~ n + 1
# k -> j + 1 ~ n + 1

for i in range(1, n + 1) :
    for j in range(i + 1, n + 1) :
        if j in iceCreamTree[i] :
            continue
        for k in range(j + 1, n + 1) :
            if k in iceCreamTree[i] or k in iceCreamTree[j] :
                continue
            
            ans += 1
    
print(ans) 
