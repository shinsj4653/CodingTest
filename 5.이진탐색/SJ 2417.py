n = int(input())
num = n
q = 0

def findSqrt(start, end) :
    if end == 0:
        return 0

    q = (start + end) // 2
    if q ** 2 >= num :
        if (q - 1) ** 2 < num:
            return q
        else :
            return findSqrt(start, q - 1)
            
    else :
        return findSqrt(q + 1, end)
    
        
print(findSqrt(1, n))
