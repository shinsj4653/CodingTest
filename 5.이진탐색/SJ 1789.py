s = int(input())
n = 1

# def findNum(start, end) :
#     n = (start + end) // 2 # 1, 55
    
#     if start > end :
#         return n
    
#     elif (n * (n + 1)) // 2 < s :
#         # left > right
#         return findNum(start, n - 1)
        
#     else :
#         return findNum(n + 1, end)

# print(findNum(1, s))

while n * (n + 1) / 2 <= s :
    n += 1
    
print(n - 1)