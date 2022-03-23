n = int(input())
l = list(map(int, input().split()))

l2 = sorted(list(set(l)))
dic = {l2[i] : i for i in range(len(l2))}
for i in l :
    print(dic[i], end = " ")

# copyl = l.copy()
# copyl.sort()
# previous = 0

# for i in range(n) :
#     idx = 0
#     for j in range(n) :
#         if copyl[i] == l[j] :
#             idx = j
#             break
        
#     if i > 0 and copyl[i] == copyl[i - 1] :
#         l[idx] = previous
    
#     else :
#         l[idx] = i
#         previous = i

# for num in l :
#     print(num, end = " ")

# for i in range(n) :
#     count = 0 
#     check = []
#     for j in range(n) :
#         if j == i :
#             continue
#         else :
#             if l[i] > l[j] and l[j] not in check :
#                 check.append(l[j])
#                 count += 1
                
#     print(count, end=" ")
