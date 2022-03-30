import sys
input = sys.stdin.readline

n, m = map(int, input().split())
strength = []

for i in range(n) :
    name, num = input().split()
    strength.append((name, int(num)))
    

def findIndex(power) :
    left = 0
    right = n - 1
    
    while left <= right :
        mid = (left + right) // 2
        if power > strength[mid][1] :
            left = mid + 1
        else :
            right = mid - 1
    print(strength[right + 1][0])
        
for i in range(m) :
    num = int(input())
    findIndex(num)
    
# # print(strength)
# start = 0

# for i in range(m) :
#     num = int(input())
#     if start == len(strength) - 1:
#         print(strength[start][0])
#         continue
    
#     for j in range(start, len(strength)) :
#         if strength[j][1] - num >= 0 :
#             print(strength[j][0])
#             start = j
#             break